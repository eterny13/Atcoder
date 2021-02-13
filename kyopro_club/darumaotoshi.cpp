// 
#include <bits/stdc++.h>
using namespace std;
int main(void){
    // Your code here!
    int ans[300];
    int ct = 0;
    while(1){
      int n;
      cin>>n;
      if(n==0) break;
      vector<int> bk(n);
      for(int i=0;i<n;i++) cin>>bk[i];
      vector<vector<int> > dp(n+1, vector<int> (n+1));

      for(int s=2;s<n+1;s++){
        for(int i=0;i<n-s+1;i++){
          int j = i+s-1;

          if((j-i == 1 || dp[i+1][j-1] == s-2) && abs(bk[i] - bk[j]) <= 1) dp[i][j] = j-i+1;
          for(int k=i;k<j;k++){
            dp[i][j] = max(dp[i][j], dp[i][k] + dp[k+1][j]);
          }
        }
      }

      /*
      for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){            
          cout << dp[i][j] << " ";
        }
        cout<<endl;
      }
      */
      ans[ct] = dp[0][n-1];
      ct++;
    }

    for(int i=0;i<ct;i++){
      cout<<ans[i]<<endl;
    }
    
}
