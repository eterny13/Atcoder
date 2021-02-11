#include <bits/stdc++.h>
using namespace std;
int main(void){
  
  int v,t,s,d;
  cin>>v>>t>>s>>d;

  double res = d/(v*1.0);

  if(t <= res && res <= s){
    cout<<"No"<<endl;
  }
  else cout<<"Yes"<<endl;

}


