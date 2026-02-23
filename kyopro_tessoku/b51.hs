import Data.List

solve :: String -> [(Int, Int)]
solve s = 
    let (_, ans) = foldl' step ([], []) (zip s [1..])
    in reverse ans
        where
            step :: ([Int], [(Int, Int)]) -> (Char, Int) -> ([Int], [(Int, Int)])
            step (stack, pairs) (char, idx)
                | char == '('   = (idx:stack, pairs) 
                | otherwise     = case stack of
                    (l:ls)  -> (ls, (l, idx):pairs)
                    []      -> ([], pairs)
    
main = do
    s <- getLine
    let ans = solve s

    mapM_ (\(a,b) -> putStrLn $ show a ++ " " ++ show b) ans
