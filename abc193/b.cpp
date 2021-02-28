#include <bits/stdc++.h>
using namespace std;
int main(void){

  int n;
  cin>>n;
  long long ans = 10e10;
  for(int i=0;i<n;i++){
    long long a,p,n;
    cin>>a>>p>>n;
    if(a < n) ans = min(ans,p);
  }

  if(ans != 10e10) cout<<ans<<endl;
  else cout<<-1<<endl;
}


