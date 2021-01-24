// http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0539
#include <bits/stdc++.h>
using namespace std;
int main(void){
    // Your code here!
    
    while(1){
        int d,n,m;
        cin>>d;
        if(d==0) break;
        cin>>n>>m;
        
        int shop[100001];
        for(int i=1;i<n;i++) cin>>shop[i];
        
        sort(shop+1, shop+n);
        
        long long ans = 0; 
        
        for(int i=1; i<=m ;i++) {
            int t;
            cin>>t;
            
            if(t<=shop[1]){
                ans += min(shop[1]-t, t);
            } 
            else{
                int left = 1, right=n, idx=1;
                while(right-left > 1){
                    int mid = (left+right)/2;
                    //cout<<mid<<endl;
                    if(t < shop[mid]){
                        right = mid-1;
                    }
                    else{
                        idx = mid;
                        left = mid+1;
                    }
                }
                if(idx == n-1) ans += min(d-t, t-shop[n-1]);
                else ans += min(t-shop[idx], shop[idx+1]-t);
            }
            
        }
        
        cout<<ans<<endl;
    }
    
}
