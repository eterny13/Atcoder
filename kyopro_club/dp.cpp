#include <bits/stdc++.h>
using namespace std;

int main(void){
  int n,m;
  cin>>n>>m;

  vector<vector<int> > dp(m+1, vector<int> (n+1, 0));

  dp[0][0] = 1;
  for(int i=1;i<=m;i++){
    for(int j=0;j<=n;j++){
      if(j -i >=0){
        dp[i][j] = dp[i][j-1] + dp[i-1][j];
      }
      else {
        dp[i][j] = dp[i-1][j];
      }
    }
  }


  for(int i=0;i<=m;i++){
    for(int j=0;j<=n;j++){
      cout << dp[i][j] << " ";
    }
    cout<<endl;
  }
  cout << dp[m][n] << endl;
}