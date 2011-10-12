{- Find the only Pythagorean triplet, {a, b, c}, for which a + b + c = 1000.

A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
    a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
-}

import Text.Printf

triplet sum = do
    let cs = reverse (takeWhile (<= sum - 3) [3,5..])
    let tri = head (concat (map (\x -> diffs sum x) cs))
    let (a, b, c) = tri
    a * b * c
diffs sum c = do
    let diff = sum - c
    let range = [1..(floor ((fromIntegral diff) / 2)) + 1]
    let triangles = filter is_triangle (map (\x -> (x, diff - x, c)) range)
    triangles
is_triangle (a, b, c) =
    a^2 + b^2 == c^2

main = do
    printf "Pythagorean triplet product having a + b + c = 1000: %d\n" (triplet 1000 :: Integer)
