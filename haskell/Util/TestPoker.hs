import Test.HUnit
import Util.Poker

testFour = [parseCard "9D", parseCard "2H", parseCard "2S", parseCard "2D", parseCard "2C"]
testThree = [parseCard "9D", parseCard "2H", parseCard "5S", parseCard "2D", parseCard "2C"]
testFull = [parseCard "9D", parseCard "2H", parseCard "9S", parseCard "2D", parseCard "2C"]
testTwo = [parseCard "9D", parseCard "2H", parseCard "9S", parseCard "2D", parseCard "5C"]
testFlush = [parseCard "9D", parseCard "2D", parseCard "KD", parseCard "JD", parseCard "5D"]
testStraight = [parseCard "9D", parseCard "TS", parseCard "JD", parseCard "QD", parseCard "KD"]
testWheel = [parseCard "2D", parseCard "3S", parseCard "4D", parseCard "5D", parseCard "AD"]

tests = TestList [ "Rank 4 of a kind" ~: FourOfAKind ~=? (fst $ rankHand testFour)
                 , "Rank 3 of a kind" ~: ThreeOfAKind ~=? (fst $ rankHand testThree)
                 , "Rank a full house" ~: FullHouse ~=? (fst $ rankHand testFull)
                 , "Rank two pair"     ~: TwoPair ~=? (fst $ rankHand testTwo)
                 , "Rank a flush"      ~: Flush ~=? (fst $ rankHand testFlush)
                 , "Rank a straight"   ~: Straight ~=? (fst $ rankHand testStraight)
                 , "Rank the wheel"    ~: Straight ~=? (fst $ rankHand testWheel)
                 ]

main = runTestTT tests
