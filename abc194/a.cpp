#include <bits/stdc++.h>
using namespace std;
int main(void){
  int a,b;
  cin>>a>>b;

  if(a+b >=15 && b >=8){
    cout<<"1"<<endl;
  }
  else if(10 <= a+b && b>=3) {
    cout<<"2"<<endl;
  }
  else if(3 <= a+b){
    cout<<"3"<<endl;
  }
  else cout<<"4"<<endl;

}

