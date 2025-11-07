
solve a b c = maximum [ct + (div (c-ct*s) l) | ct <- [0..counts]]
  where
    s = min a b
    l = max a b
    counts = div c s 


main = do
  [a,b,c] <- map read . words <$> getLine 

  print $ solve a b c
