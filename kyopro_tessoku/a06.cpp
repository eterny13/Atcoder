#include <bits/stdc++.h>
using namespace std;
int main(void){
    // Your code here!
    int n, q;
    cin>>n>>q;
    vector<int> a(n);
    
    vector<int> acc(n+1);
    for(int i=0;i<n;i++) {
        cin>>a[i];
        acc[i+1] = acc[i] + a[i];
    }
    for(int i=0;i<q;i++) {
        int l,r, ans;
        cin>>l>>r;
        
        ans = acc[r] - acc[l-1];
        
        cout << ans << endl;
    }
}
