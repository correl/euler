{- Find the only Pythagorean triplet, {a, b, c}, for which a + b + c = 1000.

A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
    a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
-}

import Text.Printf

-- |A triangle consisting of three integral sides
data Triangle = Triangle Int Int Int

-- |Return the product of the sides of the first triangle having the sum of the sides 'sum'
triplet :: Int -> Int
triplet sum = do
    let cs = reverse (takeWhile (<= sum - 3) [3,5..])
    let tri = head (concat (map (\x -> right_triangles sum x) cs))
    let (Triangle a b c) = tri
    a * b * c

-- |Find all right triangles having sum of sides 'sum' and side c length of 'c'
right_triangles :: Int -> Int -> [Triangle]
right_triangles sum c = do
    let diff = sum - c
    let range = [1..(floor ((fromIntegral diff) / 2)) + 1]
    let triangles = filter is_right_triangle (map (\x -> Triangle x (diff - x) c) range)
    triangles

-- |Return whether the provided triangle is a right triangle using the pythagorean theorem
is_right_triangle :: Triangle -> Bool
is_right_triangle (Triangle a b c) =
    a^2 + b^2 == c^2

main = do
    printf "Pythagorean triplet product having a + b + c = 1000: %d\n" (triplet 1000 :: Int)
