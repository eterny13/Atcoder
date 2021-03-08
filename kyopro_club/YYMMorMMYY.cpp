#include <bits/stdc++.h>
using namespace std;

int main(void) {
  int s;
  cin>>s;

  int s1 = s/100;
  int s2 = s%100;
  if(1 <= s1 && s1 <= 12 && 1 <= s2 && s2<= 12) {
    cout<<"AMBIGUOUS"<<endl;
  }else if(1 <= s1 && s1 <= 12){
    cout<<"MMYY"<<endl;
  }else if(1 <= s2 && s2 <= 12){
    cout<<"YYMM"<<endl;
  }
  else{
    cout<<"NA"<<endl;
  }
}