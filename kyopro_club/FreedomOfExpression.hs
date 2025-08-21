import Data.List

modv :: Integer
modv = 10^9 + 7

primeFactors :: Integer -> [Integer]
primeFactors num = go num 2 []
  where
    go 1 _ acc = acc
    go currentFactor factor acc
      | factor * factor > currentFactor = currentFactor:acc
      | mod currentFactor factor == 0   = go remain factor (factor:acc)
      | otherwise = go currentFactor (factor+1) acc
          where
            remain = div currentFactor factor

nCr :: Integer -> Integer -> Integer
nCr _ 0 = 1
nCr n r = nCr (n-1) (r-1) * n `div` r

nHr :: Integer -> Integer -> Integer
nHr n r = nCr (n+r-1) r

main = do
  [nv, m] <- map read . words <$> getLine
  let n = abs(nv)

  let val1 = product $ map (nHr m . genericLength) $ group $ primeFactors n

  let ans = mod (val1 * 2 ^ (m-1)) modv
  print ans
