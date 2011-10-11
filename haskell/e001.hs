{- Add all the natural numbers below one thousand that are multiples of 3 or 5.

    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
-}

import Text.Printf

multiples :: (Integral a) => a -> a
multiples max
    | max < 3 = 0
    | (max `mod` 5 == 0) || (max `mod` 3 == 0) = max + multiples (max - 1)
    | otherwise = multiples (max - 1)

main = do
    printf "Sum of multiples below 10: %d\n" (multiples 9 :: Int)
    printf "Sum of multiples below 1000: %d\n" (multiples 999 :: Int)
