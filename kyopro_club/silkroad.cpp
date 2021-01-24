// https://atcoder.jp/contests/joi2015yo/submissions/19238574
#include <bits/stdc++.h>
using namespace std;
int main(void){
    // Your code here!
    int n,m;
    cin>>n>>m;
    
    vector<int> city(n);
    vector<int> days(m);
    vector<vector<int>> dp(n, vector<int> (m, 10e8));
    
    for(int i=0;i<n;i++) cin>>city[i];
    for(int i=0;i<m;i++) cin>>days[i];
    for(int i=0;i<m;i++) dp[0][i] = city[0]*days[i];
    
    for(int i=1;i<n;i++){
        for(int j=i;j<=m-n+i;j++){
            for(int k=1;k<=m-n+1;k++){
                if(0 <= j-k && dp[i-1][j-k] != 10e8){
                    dp[i][j] = min(dp[i][j], dp[i-1][j-k] + city[i]*days[j]);
                }
            }
        }
    }
    
    cout << *min_element(dp[n-1].begin(), dp[n-1].end()) <<endl;
}
