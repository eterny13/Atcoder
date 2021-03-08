#include <bits/stdc++.h>
using namespace std;

int main(void) {
  int n;
  cin>>n;

  vector<vector<int> > to(n), cost(n); 
  for(int i=0;i<n-1;i++){
    int a,b,w;
    cin>>a>>b>>w;
    a--; b--;
    to[a].push_back(b);
    to[b].push_back(a);
    cost[a].push_back(w);
    cost[b].push_back(w);
  }
  queue<int> q;
  q.push(0);

  vector<int> ans(n, -1);
  ans[0] = 0;
  while(!q.empty()){
    int now = q.front();
    q.pop();
    for(int i=0;i<to[now].size();i++){
      int u = to[now][i];
      int w = cost[now][i];
      if(ans[u] != -1) continue;

      if(w%2 == 0) ans[u] = ans[now];
      else ans[u] = ans[u] = (ans[now] + 1) %2;
      q.push(u);
    }
  }

  for(int i=0;i<n;i++){
    cout << ans[i] << endl;
  }

}
