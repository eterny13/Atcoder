// http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=5148350#1
#include <bits/stdc++.h>
using namespace std;
int main(void){
    // Your code here!
    int n;
    cin>>n;
    
    int c[n];
    for(int i=0;i<n;i++) cin>>c[i]>>c[i+1];
    
    int mat[n][n]; 
    
    for(int i=0;i<n;i++){
        mat[i][i] = 0;
    }
    
    for(int i=1;i<n;i++){
        for(int j=0;j<n-i;j++){
            int idx = j + i;
            mat[j][idx] = 10e8;
            
            for(int k=j;k<idx;k++){
                mat[j][idx] = min(mat[j][idx], mat[j][k] + mat[k+1][idx] + c[j]*c[k+1]*c[idx+1]);
            }
        }
    }
    /*
    for(int i=0;i<n;i++) {
        for(int j=0;j<n;j++) {
            cout << mat[i][j] <<" ";
        }
        cout<<endl;
    }
    */
    cout << mat[0][n-1] << endl;
}
