import Data.List
import Data.Array
import Control.Monad

solve :: Int -> [(Int, Int)] -> Int
solve n abs = (sumB + sumW) `mod` md
  where
    md = 10^9 + 7
    graph = accumArray (flip (:)) [] (1, n) $ concatMap (\(u,v) -> [(u,v),(v,u)]) abs

    calc :: Int -> Int -> (Int, Int)
    calc rt u = foldl step (1,1) chsDp
      where
        chs = delete rt (graph ! u)
        chsDp = map (\c -> calc u c) chs
        step (accB, accW) (chB, chW) = (nextB, nextW)
          where
            nextB = (accB * chW) `mod` md
            nextW = (accW * (chW + chB)) `mod` md

    (sumB, sumW) = calc 1 1

main = do
  n <- readLn
  abs <- replicateM (n-1) $ do
    [a,b] <- map read . words <$> getLine :: IO [Int]
    return (a,b)

  print $ solve n abs 
