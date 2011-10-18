{-

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p  1000, is the number of solutions maximised?
-}

import Data.List
import Data.Ord
import Text.Printf
import Util.Triangle

trimap = do
    let totals = map (\x -> (x, (length . triangles) x)) [1..999]
    last (sortBy (comparing snd) totals)

triangles sum = do
    let cs = reverse (takeWhile (<= sum - 3) [3..])
    concat (map (\x -> right_triangles sum x) cs)

main = do
    printf "Maximum triangles found with sum = %d\n" (fst trimap)
