{- Find the largest palindrome made from the product of two 3-digit numbers.

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.
Find the largest palindrome made from the product of two 3-digit numbers.
-}

import Data.List (nub, sort)
import Text.Printf

is_palindrome :: (Integral a) => a -> Bool
is_palindrome n = do
    let s = (show n)
    s == (reverse s)

largest_palindrome :: (Integral a) => a -> a
largest_palindrome digits = do
    let min = 10 ^ (digits - 1)
    let max = 10 ^ digits - 1
    largest_palindrome_ min max max max 0

largest_palindrome_ :: (Integral a) => a -> a -> a -> a -> a -> a
largest_palindrome_ min max a b p
    | a < min = p
    | a * b < p || b < min = largest_palindrome_ min max (a - 1) max p
    | otherwise =
        if is_palindrome (a * b)
            then largest_palindrome_ min max a (b - 1) (a * b)
            else largest_palindrome_ min max a (b - 1) p

main = do
    printf "Largest palindrome product of 2-digit numbers: %d\n" (largest_palindrome 2 :: Integer)
    printf "Largest palindrome product of 3-digit numbers: %d\n" (largest_palindrome 3 :: Integer)
