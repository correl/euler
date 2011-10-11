{-
Find the largest prime factor of a composite number.

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
-}

import Text.Printf

pfactor :: (Integral a) => a -> [a]
pfactor n = pfactor_ n [] 2

pfactor_ n factors start =
    let next = pfactor_next n start in
    if n == next
        then n:factors
        else pfactor_ (n `div` next) (next:factors) next

pfactor_next :: (Integral a) => a -> a -> a
pfactor_next n last
    | n <= last = n
    | otherwise = head (filter (\x -> n `rem` x == 0 || n == x) [last..n])

main = do
    printf "Largest prime factor of 13195: %d\n" (head (pfactor 13195) :: Integer)
    printf "Largest prime factor of 600851475143: %d\n" (head (pfactor 600851475143) :: Integer)
