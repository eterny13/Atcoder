import Control.Monad
import Control.Monad.ST
import Data.Array.ST
import Data.Array
import qualified Data.ByteString.Char8 as C
import Data.Maybe
import Data.STRef

readInts :: IO [Int]
readInts = map (fst . fromJust . C.readInt) . C.words <$> C.getLine

solve :: Int -> Int -> [[Int]] -> Bool
solve n m es = runST $ do
  let graph = accumArray (flip (:)) [] (1,n) $ concat [[(l, (r,d)), (r, (l, -d))] | [l, r, d] <- es]
  
  visited <- newArray (1, n) False :: ST s (STUArray s Int Bool)
  potential <- newArray (1,n) 0 :: ST s (STUArray s Int Int)
  ok <- newSTRef True
  
  let dfs u p = do
        writeArray visited u True
        writeArray potential u p
      
        forM_ (graph ! u) $ \(v, d) -> do
          isVisited <- readArray visited v
          if isVisited then do
              pv <- readArray potential v
              when (pv /= p + d) $ writeSTRef ok False
          else 
              dfs v (p+d)
  
  forM_ [1..n] $ \i -> do
      isVisited <- readArray visited i
      unless isVisited $ dfs i 0
       
  readSTRef ok


main = do
  [n,m] <- readInts
  edges <- replicateM m readInts

  let ans = solve n m edges
  putStrLn $ if ans then "Yes" else "No"
