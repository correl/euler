{- What is the smallest number divisible by each of the numbers 1 to 20?

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?
-}

import Text.Printf

divisible n =
    divisible_ n n 1

divisible_ _ 1 x = x
divisible_ n c x
    | x `rem` c == 0 = divisible_ n (c - 1) x
    | otherwise = divisible_ n n (x + 1)

main = do
    printf "Foo\n"
    printf "Smallest number divisible by 1-10: %d\n" (divisible 10 :: Integer)
    printf "Smallest number divisible by 1-20: %d\n" (divisible 20 :: Integer)
