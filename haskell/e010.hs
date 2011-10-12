{- Calculate the sum of all the primes below two million.

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
-}

import Text.Printf (printf)
import Util.Primes (primes)

main = do
    printf "Sum of primes below        10: %d\n" (sum (takeWhile (<10) primes))
    printf "Sum of primes below 2,000,000: %d\n" (sum (takeWhile (<2000000) primes))
