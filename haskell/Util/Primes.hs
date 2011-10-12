module Util.Primes where

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
