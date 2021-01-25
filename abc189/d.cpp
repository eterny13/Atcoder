#include <bits/stdc++.h>
using namespace std;
int main(void){
  int n;
  cin>>n;
  vector<long long> dp(2,1);

  for(int i=0;i<n;i++){
    string s;
    cin>>s;
    vector<long long> p(2); swap(dp,p);
    for(int j=0;j<2;j++){
      for(int k=0;k<2;k++){
        int nj = j;
        if(s == "AND") nj &= k;
        else nj |= k;
        dp[nj] += p[j];
      }
    }
  }

  cout<<dp[1]<<endl;

}