#include <bits/stdc++.h>
using namespace std;

int main(void){
  int n;
  cin>>n;

  vector<int> dp(n);

  int L = 0;
  for(int i=0;i<n;i++){
    int a;
    cin>>a;
    if(i==0) {
      dp[L] = a;
      continue;
    }

    if(dp[L] < a){
      L++;
      dp[L] = a;
    }else{
      for(int j=0;j<=L;j++){
        if(dp[j] >= a){
          dp[j] = a;
          break;
        }
      }
    }
  }

  for(int i=0;i<n;i++) cout << dp[i] << " ";
  cout<<endl;
  cout << L + 1 << endl;
}