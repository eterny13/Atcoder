#include <bits/stdc++.h>
using namespace std;

int main (void) {
  int n;
  cin>>n;
  string s;
  cin>>s;

  map<char, int> m;
  m.insert(pair<char,int>('J', 0)); 
  m.insert(pair<char,int>('O', 1)); 
  m.insert(pair<char,int>('I', 2)); 
  s.insert(0,"J");
  vector<vector<int> > dp(n+1, vector<int> (8,0));
  dp[0][1] = 1;
  for(int i=1;i<=n;i++){
    int a = m[s[i-1]];
    int b = m[s[i]];

    for(int j=0;j<(1<<3);j++){
      for(int k=0;k<(1<<3);k++){
        if(!((j>>a) & 1) ) continue;
        if(!((k>>b) & 1) ) continue;
        // 前日に来ただれかはは次の日来ないといけない
        if((j & k) == 0) continue;
        dp[i][k] += dp[i-1][j];
        dp[i][k] %= 10007;
      }
    }
  }

  int ans = 0;
  for(int i=0;i<8;i++){
    ans += dp[n][i];
  }

  cout << ans%10007 << endl;
}