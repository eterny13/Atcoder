#include <bits/stdc++.h>
using namespace std;
int main(void){
  int n, x;
  cin>>n>>x;

  vector<int> a(n), r(n);
  for(int i=0;i<n;i++) cin>>a[i];

  int ct=0;  
  for(int i=0;i<n;i++){
    if(a[i] != x){
      r[ct] = a[i];
      ct++;
    }
  } 

  for(int i=0;i<ct;i++){
    cout<<r[i]<<" ";
  }
  cout<<endl;

}
