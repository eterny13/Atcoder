// https://atcoder.jp/contests/abc106/submissions/19478380
#include <bits/stdc++.h>
using namespace std;
int main(void){
    // Your code here!
    int n;
    cin>>n;
    
    int count = 0;
    for(int i=1;i<=n;){
        int ct = 1;
        for(int j=1;j<=i/2;){
            if(i%j == 0) ct++;
            j += 2;
        }
        if(ct == 8) count++;
        i += 2;
    }
    
    cout<< count << endl;
}
