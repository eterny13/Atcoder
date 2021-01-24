// http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_C
#include <bits/stdc++.h>
using namespace std;

int main(void){
    // Your code here!
    int q;
    cin>>q;
    
    for(int i=0;i<q;i++){
        string x,y;
        cin>>x;
        cin>>y;
        
        int xsize = x.size();
        int ysize = y.size();
        int ans = 0;
        
        //vector<vector<int>> dp(xsize+1, vector<int> (ysize+1));
        int dp[xsize+1][ysize+1];
        for(int i=0;i<=xsize;i++) dp[i][0] = 0;
        for(int i=0;i<=ysize;i++) dp[0][i] = 0;
        
        for(int i=1;i<=xsize;i++) {
            for(int j=1;j<=ysize;j++){
                if(x[i-1] == y[j-1]){
                    dp[i][j] = dp[i-1][j-1]+1;
                } 
                else{
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
                }
                ans = max(ans, dp[i][j]);
            }
        }
        cout<<ans<<endl;
    }
}
