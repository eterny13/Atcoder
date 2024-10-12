#include <bits/stdc++.h>
using namespace std;
int main(void){
    // Your code here!
    int h,w,n;
    cin>>h>>w>>n;
    vector<vector<int>> dp(h+1, vector<int> (w+1));
    
    for (int i=0;i<n;i++) {
        int a,b,c,d;
        cin>>a>>b>>c>>d;
        
        dp[a][b]++;
        if (c+1 <= h) dp[c+1][b]--;
        if (d+1 <= w) dp[a][d+1]--;
        if (c+1 <= h && d+1 <= w) dp[c+1][d+1]++;
    }
    
    for(int i=1;i<=h;i++) {
        for(int j = 1; j<=w;j++) {
            dp[i][j] += dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1];
        }
    }
    
    for(int i=1;i<=h;i++) {
        for(int j=1; j<=w;j++) {
            cout<< dp[i][j] << " "; 
        }
        cout<<endl;
    }
}
