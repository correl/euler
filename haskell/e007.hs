{- Find the 10001st prime.

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
-}

import Text.Printf
import Util.Primes (primes)

main = do
    printf "    6th prime: %d\n" (primes !! 5 :: Integer)
    printf "10001th prime: %d\n" (primes !! 10000 :: Integer)
