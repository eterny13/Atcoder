#include <bits/stdc++.h>
using namespace std;
int main(void){
  int n, x;
  cin>>n>>x;

  x*=100;
  int v,p,alc=0;
  for(int i=0;i<n;i++){
    cin>>v>>p;
    alc += v*p;
    if(x < alc){
      cout<<i+1<<endl;
      return 0;
    }
  }

  cout<<-1<<endl;
}


