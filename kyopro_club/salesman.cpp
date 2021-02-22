#include <bits/stdc++.h>
using namespace std;

int INF = 10e8;

int main(void){
  int nv,e;
  cin>>nv>>e;

  vector<vector<int> > G(nv, vector<int> (nv));
  vector<vector<int> > dp((1<<nv)+1, vector<int> (nv, INF));
  for(int i=0;i<e;i++){
    int u,v,d;
    cin>>u>>v>>d;
    G[u][v] = d;
  }

  dp[0][0] = 0;
  for(int i = 0;i<(1<<nv);i++){
    for(int u = 0;u<nv;u++){
      for(int v = 0;v<nv;v++){
        if((i & (1 << v)) == 0 && G[u][v] != 0) {
          cout<<i<<" "<<u<<" "<<v<<" "<<endl;
          dp[i | (1<<v)][v] = min(dp[i | (1<<v)][v], dp[i][u] + G[u][v]);
        }
      }
    }
  }
  /*
  dp[1][0] = 0;
  for(int s=1;s<(1<<nv);s++){
    for(int u=0;u<nv;u++){
      for(int v=0;v<nv;v++){
        if((s & (1<<u) != 0) && (s & (1<<v) != 0)){
          dp[s][u] = min(dp[s][u], dp[s ^ (1<<u)][v] +G[v][u]);
        }
      }
    }
  }
  */
  
  
  //cout<<dp[0][1]<<endl;
  
  for(int i=0;i<(1<<nv);i++){
    for(int j=0;j<nv;j++){
      cout<<dp[i][j]<<" ";
    }
    cout<<endl;
  }

  return 0;
}