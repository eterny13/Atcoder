#include<bits/stdc++.h>
using namespace std;

int main(void){
  int n;
  cin>>n;
  string s;
  cin>>s;

  int a  =0 ;
  int b= n-1;
  while(a <= b){
    bool left;
    for(int i=0;i<a+i <= b;i++){
      if(s[a+i] < s[b-i]){
        left = true;
        break;
      }
      else if(s[a+i] > s[b-i]){
        left = false;
        break;
      }
    }
    if(left) {
      cout << s[a];
      a++;
    }
    else{
      cout << s[b];
      b--;
    } 
  }

  cout<<endl;
}