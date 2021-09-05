// https://atcoder.jp/contests/past202005-open/tasks_print?lang=ja
// Level E

#include<bits/stdc++.h>
using namespace std;

int main(void) {
  int n,m,q;
  cin>>n>>m>>q;

  vector<vector<bool>> graph(n, vector<bool> (n, false));

  for(int i=0;i<m;i++){
    int u,v;

    cin>>u>>v;
    u--;v--;
    graph[u][v] = true;
    graph[v][u] = true;
  }

  vector<int> color(n);
  for(int i=0;i<n;i++) cin>>color[i];

  for(int i=0;i<q;i++){
    int s,x,y;   

    cin>>s;

    if(s==1){
      cin>>x;
      x--;

      cout << color[x] << endl;

      for(int i=0;i<n;i++) {
        if(graph[x][i]) {
          color[i] = color[x];
        }
      }
    }
    else {
      cin>>x>>y;
      x--;
      cout << color[x] << endl;

      color[x] = y;
    }
  }
}
