module Util.Triangle where

-- |A triangle consisting of three integral sides
data Triangle = Triangle Int Int Int
    deriving(Show, Eq)

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
