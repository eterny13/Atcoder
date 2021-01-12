// https://atcoder.jp/contests/abc188/tasks/abc188_c
#include <bits/stdc++.h>
using namespace std;
int main(void){
    // Your code here!
    int n;
    cin>>n;
    
    long long nn = pow(2,n);
    vector<int> left(nn/2), right(nn/2);
    map<int, int> mp;
    for(int i=0;i<nn/2;i++){
        cin>>left[i];
        mp[left[i]] = i+1;
    }
    long long p = nn/2 + 1;
    for(int i=0;i<nn/2;i++){
        cin>>right[i];
        mp[right[i]] = p;
        p++;
    }
    
    
    sort(left.begin(), left.end());
    sort(right.begin(), right.end());
    
    if(left[nn/2 -1] < right[nn/2-1]){
        cout<<mp[left[nn/2-1]]<<endl;
    }
    else cout<<mp[right[nn/2-1]]<<endl;
    
}
