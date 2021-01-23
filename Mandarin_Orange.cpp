// https://atcoder.jp/contests/abc189/tasks/abc189_c
#include <bits/stdc++.h>
using namespace std;
int main(void){
    // Your code here!
    int n;
    
    cin>>n;
    
    vector<int> A(n);
    set<int> s;
    long long minv = 10e8, maxv=-1;
    for(int i=0;i<n;i++){
        cin>>A[i];
        s.insert(A[i]);
    } 
    long long ans; 
    for(auto x : s){
        ans = 0;
        for(int i=0;i<n;i++){
            if(x <= A[i]) ans += x;
            else {
                maxv = max(maxv, ans);
                ans = 0;
            }
            maxv = max(maxv, ans);
        }
    }
    
    cout<<maxv<<endl;
}
