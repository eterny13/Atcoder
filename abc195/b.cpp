#include <bits/stdc++.h>
using namespace std;
int main(void){

  int a,b,w;
  cin>>a>>b>>w;
  w*=1000;

  int ans1=10e8;
  int ans2=-1;
  for(int i=a;i<=b;i++){
    for(int j=0;j<=w/i;j++){
        if((w-i*j)% == 0){
          ans1=min(ans1, j+((w-i*j)/k));
          ans2=max(ans2, j+((w-i*j)/k));
        }
    }
  }

  if(ans1==10e8 && ans2 ==-1) cout<<"UNSATISFIABLE"<<endl;
  else cout<<ans1<<" "<< ans2<<endl;
}


