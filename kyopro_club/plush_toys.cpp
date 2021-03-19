#include <bits/stdc++.h>
using namespace std;

int main(void) {
  int n,m;
  cin>>n>>m;
  vector<int> cnt(m,0);
  const int INF = 10e8;

  vector<vector<int>> sum(m, vector<int> (n+1));
  vector<vector<int>>  dp(1<<m, vector<int> (m, INF));

  for(int i=0;i<n;i++){
    int t;
    cin>>t;
    t--;
    cnt[t]++;
    sum[t][i]=1;
  }

  for(int i=0;i<m;i++){
    for(int j=1;j<n;j++){
      sum[i][j] += sum[i][j-1];
    }
  }

  for(int i=0;i<m;i++){
    dp[1<<i][i] = sum[i][cnt[i]] - sum[i][0];
    cout << sum[i][cnt[i]] - sum[i][0];
  }

  for(int b=0;b<(1<<m);b++){
    for(int sh=0;sh<m;sh++){
      if((b>>sh)&1) {
        for(int nt=0;nt<m;nt++){
          if(!((b>>nt)&1)){
            int l = 0;
            for(int i=0;i<m;i++) if((b>>i)&1) l += cnt[i];
            cout << l << endl;
            cout << sum[nt][l + cnt[nt]] << endl;
            

            int cur = sum[nt][l + cnt[nt]] - sum[nt][l];
            cout << cur << endl;

            dp[b | (1<<nt)][nt] = min(dp[b | (1<<nt)][nt], dp[b][sh] + cur);
          }
        }
      }
    }
  }

  int ans = INF;
  for(int i=0;i<m;i++){
    ans = min(ans, dp[(1<<m)-1][i]);
  }

  cout << ans << endl;

}
