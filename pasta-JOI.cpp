// https://atcoder.jp/contests/joi2012yo/submissions/18686308
#include <bits/stdc++.h>
using namespace std;
int main(void){
    // Your code here!
    int N,K;
    cin>>N>>K;
    
    vector<int> p(N, -1);
    for(int i=0;i<K;i++){
        int a,b;
        cin>>a>>b;
        p[a-1] = b-1;
    }
    
    long long dp[101][3][3]={0};
    dp[0][0][0] = 1; 
    
    for(int i=1;i<N+1;i++){
        for(int j=0;j<3;j++){
            for(int k=0;k<3;k++){
                vector<int> s = {0,1,2};
                if(p[i-1] >= 0){
                    s = {p[i-1]};
                } 
                
                for(int v : s){
                    if(i >= 3 && j==k && k==v) continue;
                    dp[i][k][v] = (dp[i][k][v] + dp[i-1][j][k]) % 10000;
                }
            }
        }
    }
    
    long long ans=0;
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
                //cout<< dp[3][i][j] << " ";
                ans = (ans + dp[N][i][j]) % 10000;
        }
    }
    
    cout << ans << endl;
}
