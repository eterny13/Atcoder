import Data.Char
import Data.List
import Data.Ord 
import qualified Data.Vector as V
import qualified Data.Map.Strict as M
import qualified Data.ByteString.Char8 as BS

readIntList :: IO [Int]
readIntList = unfoldr (BS.readInt . BS.dropWhile isSpace) <$> BS.getLine

solve :: Int -> V.Vector Int -> Int
solve n ws = table M.! (0, n-1)
  where
    sums = V.scanl' (+) 0 ws
    getSum i j = (sums V.! (j+1)) - (sums V.! i)

    -- 区間の長さが1
    dp_len1 = M.fromList [((i, i), 0) | i <- [0..n-1]]
    -- 区間の長さが2
    dp_len2 = M.fromList [((i, i+1), getSum i (i+1)) | i <- [0..n-2]]

    dp_base :: M.Map (Int, Int) Int
    dp_base = M.union dp_len1 dp_len2

    -- Cutテーブル
    cut_base = M.fromList [((i, i+1), i) | i <- [0..n-2]]

    (table, _) = foldl go (dp_base, cut_base) [2..n]

    go :: (M.Map (Int, Int) Int, M.Map (Int, Int) Int) -> Int -> (M.Map (Int, Int) Int, M.Map (Int, Int) Int)
    go (dp, cut) len = (updatedDP, updatedCut)
      where
        newEntries = [calculateEntry dp cut j (j+len) | j <- [0..n-len-1]]
        -- DPとCutに分解
        (new_dp_entries, new_cut_entries) = unzip $ map (\(((ji, cost), k)) -> ((ji, cost), (ji, k))) newEntries
        updatedDP  = M.union dp  $ M.fromList new_dp_entries
        updatedCut = M.union cut $ M.fromList new_cut_entries

    -- [j, i] の最小コストと最適な分割点kを計算
    calculateEntry :: M.Map (Int, Int) Int -> M.Map (Int, Int) Int -> Int -> Int -> (((Int, Int), Int), Int)
    calculateEntry dp cut j i = (((j, i), totalCost), bestK)
      where
        c1 = cut M.! (j, i - 1)
        c2 = cut M.! (j + 1, i)
        candidates = [c1..c2]
        -- first case (3, 0), (5,1)
        costs = [( (dp M.! (j, k)) + (dp M.! (k + 1, i)), k) | k <- candidates]
        (minSubCost, bestK) = minimumBy (comparing fst) costs
        totalCost = minSubCost + getSum j i
        
main = do
  n <- readLn 
  ws <- readIntList
  let ws' = V.fromList ws
  let ans = solve n ws'
  print ans
