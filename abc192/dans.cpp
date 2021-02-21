#include <bits/stdc++.h>
using namespace std;

int main(void) {

  string x;
  long long m;
  cin>>x>>m;

  if(x.size() == 1){
    if(stoi(x) <= m) cout<<1<<endl;
    else cout<<0<<endl;
    return 0;
  }

  int maxe = -1;
  for(int i=0;i<x.size();i++) maxe = max(maxe, int(x[i]-'0'));
  
  long long l=maxe, r=m+1;
  while(r-l > 1){
    long long mid = (l+r)/2;
    long long v = 0;

    for(int i=0;i<x.size();i++){
      if(v > m/mid) v = m + 1;
      else v = v*mid + int(x[i]-'0');
      //cout<<v<<endl;
    }
    if(v <= m) l = mid;
    else r = mid;
  }
  cout<<l - maxe<<endl;
  return 0;
}

