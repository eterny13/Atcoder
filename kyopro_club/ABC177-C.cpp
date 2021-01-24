#include <bits/stdc++.h>
using namespace std;
int main(void){
    // Your code here!
    const int m = 1000000007;
    int n;
    cin>>n;
    vector<int> nu(n);
    int ct=0;
    for(int i=0;i<n;i++){ 
        cin>>nu[i];
    }
    
    
    int ans=0;
    int x=0;
    for(int i=0;i<n;i++){
        ans = (ans+(long long)nu[i]*x)%m;
        x = (x+nu[i])%m;
    }
    
    cout<<ans<<endl;
    
}
