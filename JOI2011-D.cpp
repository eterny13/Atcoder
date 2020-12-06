// https://atcoder.jp/contests/joi2011yo/submissions/me
#include <bits/stdc++.h>
using namespace std;
int main(void){
    // Your code here!
    int n;
    cin>>n;
    
    vector<int> num(n);
    vector<vector<long long>> dp(n, vector<long long> (21,0));
    
    for(int i=0;i<n;i++) {
        cin>>num[i];
    }
     
    for(int i=0;i<=20;i++) dp[0][i] = 0;
    for(int i=0;i<=20;i++) dp[1][i] = 0;
    dp[1][num[0]] = 1;
    
    for(int i=1;i<n-1;i++){
       for(int j=0;j<=20;j++) {
           if(0 <= j-num[i] && j+num[i] <= 20){
                dp[i+1][j] = dp[i][j-num[i]] + dp[i][j+num[i]];
           }else if(0 <= j-num[i] && j+num[i] > 20){
                dp[i+1][j] = dp[i][j-num[i]];
           }else if(0 > j-num[i] && j+num[i] <= 20) {
                dp[i+1][j] = dp[i][j+num[i]];
           }
       }
    }
    cout<<dp[n-1][num[n-1]]<<endl;
}
