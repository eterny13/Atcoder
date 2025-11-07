import Data.Char
import Data.List
import Data.Array.ST
import Data.Array.Unboxed
import Control.Monad
import Control.Monad.ST
import qualified Data.ByteString.Char8 as BS

readIntList :: IO [Int]
readIntList = unfoldr (BS.readInt . BS.dropWhile isSpace) <$> BS.getLine

modulo = 10^9 + 7

solve :: Int -> Int -> [[Int]] -> Int
solve h w cols = calculatePaths h w grid
  where
    cs = concat cols
    grid = listArray ((0,0),(w-1,h-1)) cs

calculatePaths :: Int -> Int -> Array (Int, Int) Int -> Int
calculatePaths h w grid = runST $ do
  let bounds = ((0,0),(w-1,h-1))
  memo <- newArray bounds (-1) :: ST s (STUArray s (Int, Int) Int)

  let dfs (x,y) = do
        v <- readArray memo (x,y)
        if v /= -1
          then return v
        else do
          let d1 = [(x,y+1) | y < h-1,  grid ! (x, y+1) > grid ! (x,y)]
          let d2 = [(x,y-1) | y > 0,    grid ! (x, y-1) > grid ! (x,y)]
          let d3 = [(x+1,y) | x < w-1,  grid ! (x+1, y) > grid ! (x,y)]
          let d4 = [(x-1,y) | x > 0,    grid ! (x-1, y) > grid ! (x,y)]
          let neighbors = d1:d2:d3:d4:[]
          neighborPathCount <- mapM dfs neighbors
          let total = foldl' (\acc c -> mod (acc + c) modulo) 1 neighborPathCount
          writeArray memo (x,y) total
          return total

  forM_ (range bounds) dfs
  allPathCount <- getElems memo
  return $ foldl' (\acc c -> mod (acc + c) modulo) 0 allPathCount

main = do
  [h,w] <- map read . words <$> getLine
  rows <- replicateM h $ readIntList
    
  let cols = transpose rows
  
  print $ solve h w cols
