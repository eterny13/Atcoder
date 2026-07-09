import Control.Monad
import Data.Array
import Data.Maybe
import qualified Data.ByteString.Char8 as C

readInt :: C.ByteString -> Int
readInt = fst . fromJust . C.readInt

parseEdges :: Int -> [C.ByteString] -> [(Int, Int, Int)]
parseEdges 0 _ = []
parseEdges i (u:v:w:rest) = (readInt u, readInt v, readInt w) : parseEdges (i-1) rest
parseEdges _ _ = []

solve :: Int -> [(Int, Int, Int)] -> Array Int Int
solve n uvs = colors
  where
    g = accumArray (flip (:)) [] (1,n) $ concatMap (\(u,v,w) -> [(u, (v,w)), (v, (u,w))]) uvs
    colors = array (1,n) (dfs 1 0 0)
    dfs u p c = (u,c): concatMap (\(v, w) -> if v == p then [] else dfs v u (judge c (mod w 2))) (g ! u)
    judge c w = if w == c then 0 else 1 

main = do
  ws <- C.words <$> C.getContents
  case ws of
      (nStr:rest) -> do
          let n = readInt nStr
          let edges = parseEdges (n-1) rest
          let cs = solve n edges
          putStr $ unlines $ [show (cs ! i) | i <- [1..n]]
      [] -> return ()
