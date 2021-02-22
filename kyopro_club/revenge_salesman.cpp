#include <bits/stdc++.h>
using namespace std;

#define ll long long
const ll INF = 1e18;
int main(void){
  ll nv,e;
  cin>>nv>>e;

  if(nv == 1){
    cout<<"1 0"<<endl;
    return 0;
  }

  vector<vector<ll> > G(nv, vector<ll> (nv));
  vector<vector<ll> > t(nv, vector<ll> (nv));
  vector<vector<ll> > dp((1<<nv)+1, vector<ll> (nv, INF));
  vector<vector<ll> > ct((1<<nv)+1, vector<ll> (nv));
  for(int i=0;i<e;i++){
    ll u,v,d,ti;
    cin>>u>>v>>d>>ti;
    u--; v--;
    G[u][v] = G[v][u] = d;
    t[u][v] = t[v][u] = ti;
  }
  

  dp[0][0] = 0;
  ct[0][0] = 1; 
  for(int i = 0;i<(1<<nv);i++){
    for(int u = 0;u<nv;u++){
      for(int v = 0;v<nv;v++){
        if((i & (1 << v)) == 0 && G[u][v] != 0) {
          if(dp[i][u] + G[u][v] <= t[u][v]){
            //cout<<i<<" "<<u<<" "<<v<<" "<<endl;
            if(dp[i][u] + G[u][v] == dp[i | (1<<v)][v]){
              ct[i | (1<<v)][v] += ct[i][u];
            }
            else if(dp[i | (1<<v)][v] > dp[i][u] + G[u][v]){
              //dp[i | (1<<v)][v] = min(dp[i | (1<<v)][v], dp[i][u] + G[u][v]);
              dp[i | (1<<v)][v] = dp[i][u] + G[u][v];
              ct[i | (1<<v)][v] = ct[i][u];
            }
          }
        }
      }
    }
  }
  
  /*
  for(int i=0;i<(1<<nv);i++){
    for(int j=0;j<nv;j++){
      cout<<dp[i][j]<<" ";
    }
    cout<<endl;
  }
  for(int i=0;i<(1<<nv);i++){
    for(int j=0;j<nv;j++){
      cout<<ct[i][j]<<" ";
    }
    cout<<endl;
  }
  */

  if(dp[(1<<nv)-1][0] >= INF){
    cout<<"IMPOSSIBLE"<<endl;
  }
  else cout<<dp[(1<<nv)-1][0]<<" "<<ct[(1<<nv)-1][0]<<endl;
  return 0;
}