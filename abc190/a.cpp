#include <bits/stdc++.h>
using namespace std;
int main(void){
  int a,b,c;
  cin>>a>>b>>c;

  if(c==0){
    while(a>=0 && b >=0){
      a--;
      if(a<0){
        cout<<"Aoki"<<endl;
        return 0;
      }
      b--;
      if(b<0){
        cout<<"Takahashi"<<endl;
        return 0;
      }

    }
  }
  else{
    while(a>=0 && b >=0){
      b--;
      if(b<0){
        cout<<"Takahashi"<<endl;
        return 0;
      }
      a--;
      if(a<0){
        cout<<"Aoki"<<endl;
        return 0;
      }
    }
  }
}


