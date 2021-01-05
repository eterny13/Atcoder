// https://atcoder.jp/contests/joi2013yo/submissions/18903007
#include <bits/stdc++.h>
using namespace std;
int main(void){
    // Your code here!
    
    int D,M;
    cin>>D>>M;
    
    vector<int> Ds(D);
    for(int i=0;i<D;i++) cin>>Ds[i];
    
    vector<int> A(M);
    vector<int> B(M);
    vector<int> C(M);
    for(int i=0;i<M;i++){
        cin>>A[i]>>B[i]>>C[i];
    }
    
    vector<vector<int>> dp (D+1, vector<int> (M, -10000));
    for(int i=0;i<M;i++) dp[0][i] = 0;
   
    for(int i=0;i<D;i++){
        int p = Ds[i]; 
        for(int j=0;j<M;j++){
            if(A[j] <= p && p <= B[j]){
                if(i==0){
                    dp[i+1][j] = dp[i][j];
                }
                else{
                    for(int k=0;k<M;k++){
                        dp[i+1][j] = max(dp[i][k] + abs(C[j]-C[k]), dp[i+1][j]);
                    }
                }
            }
        }
    }
    
    cout<< *max_element(dp[D].begin(), dp[D].end()) << endl;
}
