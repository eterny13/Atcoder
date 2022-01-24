// https://atcoder.jp/contests/joi2013ho/submissions/28780435
#include <bits/stdc++.h>
using namespace std;
int main(void){
    // Your code here!
    int n;
    cin>>n;
    vector<int> l(n);
    vector<int> a(0);
    
    for(int i=0;i<n;i++) cin>>l[i];
    
    int cnt=0, prv=-1;
    for(int i=0;i<n;i++){
        if(prv == l[i]){
            a.push_back(cnt);
            cnt = 1;
        }
        else {
            cnt++;
        }
        prv = l[i];
    }
    a.push_back(cnt);
    
    a.push_back(0);
    a.push_back(0);
   
    long long ans = -1;
    for(int i=0;i<a.size()-2;i++){
        long long sumv = 0;
        for(int j=0;j<3;j++){
            sumv += a[i+j];
        }
        //cout << a[i] << endl;
        ans = max(ans, sumv);
    }
    
    cout << ans << endl;
}
