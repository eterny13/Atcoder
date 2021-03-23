#include<bits/stdc++.h>
using namespace std;

int main(void){
  int L;
  cin>>L;

  long long ans=1;
  for(int i=1;i<=11;i++){
    ans *= L-i;
    # かけるたびに割らないとオーバーフローする
    ans /= i;
  }
  cout<<ans<<endl;
}