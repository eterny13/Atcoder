#include <bits/stdc++.h>
using namespace std;
int main(void){
  string s;
  cin>>s;

  int cnt=0;
  for(int i=0;i<s.size();i++){
    if((i+1)%2 == 0){
      if(isupper(s[i])) cnt++;
    }else{
      if(!isupper(s[i])) cnt++;
    }
  }

  if(s.size() == cnt) cout<<"Yes"<<endl;
  else cout<<"No"<<endl;
}
