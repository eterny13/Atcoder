#include <bits/stdc++.h>
using namespace std;
int main(void){
  int n,m,q;
  cin>>n>>m>>q;

  vector<int> w(n), v(n);
  for(int i=0;i<n;i++){
    cin>>w[i]>>v[i];
  }
  vector<int> x(m);
  for(int i=0;i<m;i++) cin>>x[i];
  for(int i=0;i<q;i++){
    int l,r;
    cin>>l>>r;
    l--; r--;
    int ans = 0;
    vector<int> xd;
    for(int j = 0;j<m;j++){
      if(j < l || r < j){
        xd.push_back(x[j]);
      }
    }
    sort(xd.begin(),xd.end());
    vector<bool> fl(n);
    for(int j=0;j<xd.size();j++){
      pair<int,int> M (-1,-1);
      for(int k=0;k<n;k++){
        if(xd[j] >= w[k] && !fl[k]){
          M = max(M, pair<int,int>(v[k],k));
        }
      }
      if(M.second != -1){
        fl[M.second] = true;
        ans += M.first;
      }
    }

    cout << ans << endl;
  }


}