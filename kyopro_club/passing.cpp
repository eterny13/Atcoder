// https://atcoder.jp/contests/typical90/submissions/32816835
// using dijkstra
#include <bits/stdc++.h>
using namespace std;


void dijkstra(vector<vector<pair<int,int>>> g, vector<int> &costs, int s, int t){
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int,int>>> q;
    
    //if(s==t) return 0;
    // cost, node_id
    q.push(make_pair(0, s));
    costs[s] = 0;
    
    
    while(!q.empty()){
        int now = q.top().second;
        int cost = q.top().first;
        q.pop();
        
        for(int i=0; i < g[now].size(); i++){
            int nxt = g[now][i].first;
            int nxt_cost = g[now][i].second;

            if(costs[nxt] > cost + nxt_cost){
                //cout << next << endl;
                costs[nxt] = cost + nxt_cost;
                q.push(make_pair(costs[nxt], nxt));
            }
        }
    }
}

int main(void){
    // Your code here!
    const int INF = 10e10;
    
    int n,m;
    cin>>n>>m;
    vector<vector<pair<int, int>>> g(n+1);
    
    int a,b,c;
    for(int i=0;i<m;i++){
        cin>>a>>b>>c;
        g[a].push_back(make_pair(b,c));
        g[b].push_back(make_pair(a,c));
    }
    
    vector<int> scost(n+1,INF);
    vector<int> tcost(n+1,INF);
    
    dijkstra(g, scost, 1, n);
    dijkstra(g, tcost, n, 1);
        
    //cout << n << endl;
    for(int i=1;i<=n;i++){
        cout << scost[i] + tcost[i] << endl;
    }
    
    return 0;
}
