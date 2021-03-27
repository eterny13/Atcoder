#include<bits/stdc++.h>
using namespace std;

int main(void){
  long long n,m,k;
  cin>>n>>m>>k;

  vector<long long> A(n+1);
  vector<long long> B(m+1);

  for(int i=1;i<=n;i++) cin>>A[i], A[i]+=A[i-1];
  for(int i=1;i<=m;i++) cin>>B[i], B[i]+=B[i-1];
  vector<long long> ans;
  for(int i=0;i<=n;i++){
    for(int j=m;j>=0;j--){
      if(A[i] + B[j] <= k){
        ans.push_back(i+j);
        m=j;
        break;
      }
    }
  }

  cout << *max_element(ans.begin(), ans.end()) << endl;
}
