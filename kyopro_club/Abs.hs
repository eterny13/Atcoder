import Data.Array
import Data.Array.IO
import Data.Array.ST
import Control.Monad
import Control.Monad.ST

solve :: Int -> Int -> Int -> [Int] -> Int
solve n z w as = runST $ do
    memo <- newArray ((0,0), (n-1, 1)) (-1) :: ST s (STUArray s (Int, Int) Int)
    let as_array = array (0, n-1) (zip [0..n-1] as)
    func n 0 0 z w as_array memo

func :: Int -> Int -> Int -> Int -> Int -> Array Int Int -> STUArray s (Int, Int) Int -> ST s Int
func n id turn z w as memo = do
  if id == n then
    return $ abs (z-w)
  else do
    v <- readArray memo (id, turn)
    if v /= -1 then
      return v
    else do
      result <- if turn == 0 
        then do
          results <- forM [id..n-1] $ \i ->
            func n (i+1) (1-turn) (as ! i) w as memo 
          return $ maximum results
        else do
          results <- forM [id..n-1] $ \i ->
            func n (i+1) (1-turn) z (as ! i) as memo
          return $ minimum results

      writeArray memo (id, turn) result 
      return result
    
main = do
  [n,z,w] <- map read . words <$> getLine
  as <- map read . words <$> getLine

  print $ solve n z w as
