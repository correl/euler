{-
Find the largest prime factor of a composite number.

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
-}

import Text.Printf

pfactor :: (Integral a) => a -> [a]
pfactor n = pfactor_ n []

pfactor_ :: (Integral a) => a -> [a] -> [a]
pfactor_ n factors = do
    let next = pfactor_next n 2
    if next == n
        then factors ++ [n]
        else pfactor_ (n `div` next) (factors ++ [next])

pfactor_next :: (Integral a) => a -> a -> a
pfactor_next n factor
    | n == factor = factor
    | n `rem` factor == 0 = factor
    | otherwise = pfactor_next n (factor + 1)

main = do
    printf "Largest prime factor of 600851475143: %d\n" (last (pfactor 600851475143) :: Int)
