// http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A&lang=jp
#include <bits/stdc++.h>
using namespace std;
int main(void){
    // Your code here!
    int N,M;
    cin>>N>>M;
    
    vector<int> c(M);
    int dp[M+1][N+1];
    for(int i=0;i<=M;i++){
        for(int j=0;j<=N;j++) dp[i][j] = 10e8;
    }
    for(int i=0;i<M;i++){
        cin>>c[i];
    }
    
    dp[0][0] = 0;
    for(int i=0;i<M;i++){
        for(int j=0;j<N+1;j++){
            if(j-c[i] >= 0) {
                dp[i+1][j] = min(dp[i+1][j-c[i]]+1, dp[i][j]);
            }            
            else dp[i+1][j] = dp[i][j];
        }
    }
    
    cout<<dp[M][N]<<endl;
    
}
