import Control.Monad
import Control.Monad.ST
import Data.Array.ST
import Data.Array.Unboxed

buildAdj :: Int -> [(Int, Int, Int)] -> Array Int [(Int, Int)]
buildAdj n edges = accumArray (flip (:)) [] (1, n) $ concatMap (\(u, v, w) -> [(u, (v, w)), (v, (u, w))]) edges

solve :: Int -> [(Int, Int, Int)] -> UArray Int Int
solve n edges = runSTUArray $ do
  colors <- newArray (1,n) (-1) :: ST s (STUArray s Int Int)
  let g = buildAdj n edges

  let dfs [] = return ()
      dfs ((u,p,c) : ss) = do
        visited <- readArray colors u
        if visited /= -1
          then dfs ss
          else do 
            writeArray colors u c
            let next = [(v, u, if c == (mod w 2) then 0 else 1) | (v, w) <- g ! u, v /= p]
            dfs (next ++ ss)
  dfs [(1,0,0)]
  return colors

main = do 
  n <- readLn
  edges <- replicateM (n-1) $ do
    [u,v,w] <- map read . words <$> getLine :: IO [Int]
    return (u,v,w)

  let cs = solve n edges
  putStrLn $ unlines $ map (show . (cs !)) [1..n]
