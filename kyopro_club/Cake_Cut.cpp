#include <bits/stdc++.h>
using namespace std;
int n;
vector<int> s;
vector<vector<int> > dp;

long long func(int i, int j, int ct){
  if(dp[i][j]) return dp[i][j];
  if(i==j) {
    if(ct%2 == 1) return dp[i][j] ;
    else return dp[i][j] = s[i];
  }
  
  if(ct%2 == 1){
    if(s[i] < s[j]){
      dp[i][j] = func(i, (j+n-1)%n, ct+1);
      return dp[i][j];
    }else{
      dp[i][j] = func((i+1)%n, j, ct+1);
      return dp[i][j];
    } 
  }
  else{
    return dp[i][j] = max(func((i+1)%n, j, ct+1) + s[i], func(i, (j+n-1)%n, ct+1) + s[j]);
  }
}

int main(void){
  cin>>n;

  s.resize(n);
  dp.resize(n, vector<int> (n));
  for(int i=0;i<n;i++){
    cin>>s[i];
  }

  long long ans=-1;
  for(int i=0;i<n;i++){
    ans = max(ans, func((i+1)%n, (i+n-1)%n, 1) + s[i]);
  }

  cout << ans << endl;
}