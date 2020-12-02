// https://atcoder.jp/contests/abc183/tasks/abc183_c
#include <bits/stdc++.h>
using namespace std;
int main(void){
    // Your code here!
    int n,k;
    cin>>n>>k;
    
    int town[n][n];
    vector<int> v(n-1);
    for(int i=0;i<n-1;i++) v[i] = i+1;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
           cin>>town[i][j];
        }
    }
    int p = 0; 
    int ans = 0;
    int cnt = 0;
    do{
       for(int n:v){
          ans += town[p][n]; 
          p = n;
       }
       ans += town[p][0];
       if(ans == k) cnt++;
       ans = 0;
       p = 0;
    }while(next_permutation(v.begin(), v.end()));
    
    cout<<cnt<<endl;
}
