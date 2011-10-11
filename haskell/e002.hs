{-
Find the sum of all the even-valued terms in the Fibonacci sequence which do not exceed four million.

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Find the sum of all the even-valued terms in the sequence which do not exceed four million.
-}

import Text.Printf

fib :: (Integral a) => (a, a) -> a
fib (x, y) = x + y

fibnext :: (Integral a) => (a, a) -> (a, a)
fibnext (x, y) = (y, x + y)

fibsumeven :: (Integral a) => a -> a
fibsumeven max = fibsumeven_ max 0 (0,1)

fibsumeven_ :: (Integral a) => a -> a -> (a, a) -> a
fibsumeven_ max total pair
    | fib pair > max = total
    | even (fib pair) = fibsumeven_ max (total + (fib pair)) (fibnext pair)
    | otherwise = fibsumeven_ max total (fibnext pair)

main = do
    printf "Sum of even fibonacci terms <= 4,000,000: %d\n" (fibsumeven 4000000 :: Int)
