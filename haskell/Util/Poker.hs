module Util.Poker where

import Data.Char (digitToInt)
import Data.List (sort, sortBy, group)
import Data.Ord (comparing)

data Suit = Hearts | Diamonds | Clubs | Spades
        deriving (Show, Eq, Ord)

data Card = Card { cardValue :: Int
                 , cardSuit  :: Suit
                 }
                 deriving (Show)

instance Eq Card where
    x == y = (cardValue x) == (cardValue y)
    x /= y = (cardValue x) /= (cardValue y)

instance Ord Card where
    compare x y = compare (cardValue x) (cardValue y)

parseCard :: String -> Card
parseCard s = parseCard' $ break (\x -> notElem x ('A':'K':'Q':'J':'T':['0'..'9'])) s

parseCard' :: (String, String) -> Card
parseCard' (v, s) = Card v' s'
                    where v' = case v of
                              "T" -> 10
                              "J" -> 11
                              "Q" -> 12
                              "K" -> 13
                              "A" -> 14
                              _   -> foldl (\x y -> x * 10 + y) 0 $ map (digitToInt) v
                          s' = case s of
                              "H" -> Hearts
                              "D" -> Diamonds
                              "C" -> Clubs
                              "S" -> Spades
                              _   -> error "Unknown card suit"

type Hand = [Card]

data HandRank = HighCard
              | OnePair
              | TwoPair
              | ThreeOfAKind
              | Straight
              | Flush
              | FullHouse
              | FourOfAKind
              | StraightFlush
              | RoyalFlush
              deriving(Show, Eq, Ord)

type HandValue = (HandRank, [Int])

rankHand :: Hand -> HandValue
rankHand h
    | biggestSet > 1 = rankSets grouped
    | isFlush h && isStraight h = (StraightFlush, cardValues $ fixStraight h')
    | isFlush h = (Flush, cardValues h')
    | isStraight h = (Straight, cardValues $ fixStraight h')
    | otherwise = (HighCard, cardValues h')
    where h' = take 5 $ reverse $ sort h
          grouped = sets $ take 5 h
          biggestSet = length $ head grouped

rankSets :: [[Card]] -> HandValue
rankSets (x:xs) = case (length x) of
                      4 -> (FourOfAKind, values)
                      1 -> (HighCard, cardValues $ concat (x:xs))
                      _ -> case rest of
                               (OnePair, values') -> case l of 3 -> (FullHouse, (cardValue $ head x) : values')
                                                               2 -> (TwoPair, (cardValue $ head x) : values')
                                                               _ -> (OnePair, values)
                               _ -> case l of 3 -> (ThreeOfAKind, values)
                                              _ -> (OnePair, values)
                  where l = length x
                        rest = rankSets $ filter (\x' -> length x' <= l) xs
                        values = (cardValue $ head x) : (take 1 $ cardValues $ concat xs)
rankSets [] = (HighCard, [])

cardValues :: [Card] -> [Int]
cardValues = map (cardValue)

sets :: Hand -> [[Card]]
sets h = reverse $ sortBy (comparing (\x -> length x)) $ group $ sort h

isFlush :: Hand -> Bool
isFlush h = suits == 5
            where groups = reverse $ sortBy (comparing (\x -> length x)) $ group $ sort $ map (cardSuit) h
                  suits = length $ head groups

isStraight :: Hand -> Bool
isStraight h = isStraight' $ sort $ cardValues h

isStraight' :: [Int] -> Bool
isStraight' [] = False
isStraight' (2:3:4:5:14:[]) = True
isStraight' xs = xs == [(head xs) .. (last xs)]

fixStraight :: Hand -> Hand
fixStraight (x:xs)
    | 2 `elem` values && 14 `elem` values = xs ++ [(Card 1 (cardSuit x))]
    | otherwise = (x:xs)
    where values = cardValues (x:xs)
