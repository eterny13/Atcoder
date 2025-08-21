import Data.Array
import Data.Array.IO
import Data.Array.ST
import Control.Monad
import Control.Monad.ST
import qualified Data.Vector.Unboxed as UV
import qualified Data.Vector.Unboxed.Mutable as MV


solve :: Int -> Int -> Int -> MV.STVector s Int -> MV.STVector s Int -> STUArray s (Int, Int) Int -> ST s Int
solve i j current as bs dp = do

  memo <- readArray dp (i, j)
  if memo /= -1 then return memo
  else do
    let lenA = MV.length as
    let lenB = MV.length bs
    if i == lenA && j == lenB then return 0
    else do
      let point = 0

      -- first deck
      res1 <- if i < lenA then do
                val <- MV.read as i
                next <- solve (i+1) j (current - val) as bs dp
                return $ current - next
              else
                return point 
      -- second deck
      res2 <- if j < lenB then do
                val <- MV.read bs j
                next <- solve i (j+1) (current - val) as bs dp
                return $ current - next
              else
                return point
      let finalpoint = max res1 res2        
      writeArray dp (i, j) finalpoint
      return finalpoint


main = do
  [a,b] <- map read . words <$> getLine
  as <- map read . words <$> getLine
  bs <- map read . words <$> getLine

  let total = sum as + sum bs

  ans <- return $ runST $ do
    dp <- newArray ((0,0), (a, b)) (-1) :: ST s (STUArray s (Int, Int) Int)

    as' <- MV.new a
    forM_ (zip [0..] as) $ \(idx, val) -> MV.write as' idx val

    bs' <- MV.new b 
    forM_ (zip [0..] bs) $ \(idx, val) -> MV.write bs' idx val

    solve 0 0 total as' bs' dp
  
  print ans
