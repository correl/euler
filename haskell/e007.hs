{- Find the 10001st prime.

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
-}

import Text.Printf

is_prime :: (Integral a) => a -> Bool
is_prime n
    | n == 1 = False
    | n < 4 = True
    | n `rem` 2 == 0 = False
    | n < 9 = True
    | n `rem` 3 == 0 = False
    | otherwise = do
        let f = sqrt (fromIntegral n)
        let checkprime x = (n `rem` x == 0 || n `rem` (x + 2) == 0)
        not (or (map checkprime (takeWhile (<= floor f) [5,11..])))

primes = filter is_prime (2:[3,5..])

main = do
    printf "    6th prime: %d\n" (primes !! 5 :: Integer)
    printf "10001th prime: %d\n" (primes !! 10000 :: Integer)
