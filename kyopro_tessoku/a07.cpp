#include <bits/stdc++.h>
using namespace std;
int main(void){
    // Your code here!
    int d,n;
    cin>>d>>n;
    vector<int> acc(d+1);
    
    for(int i=0;i<n;i++) {
        int l,r;
        cin>>l>>r;
        acc[l]++;
        acc[r+1]--;
    }
    
    for(int i=0;i<d;i++) {
        acc[i+1] += acc[i];
    }
    
    for(int i=0;i<d;i++){
        cout<<acc[i+1]<<endl;
    }
}
