// https://atcoder.jp/contests/joi2009yo/tasks/joi2009yo_d
#include <bits/stdc++.h>
using namespace std;
int n,m;
int ans=-1;
bool check(int x, int y){
    return x >= 0 && x < n && y >= 0 && y < m;
}

void dfs(vector<vector<int>> &mas, int x, int y, int ct){
    
    mas[y][x] = 0;       
    ans = max(ans, ct);
    int vy[4] = {-1, 0, 0, 1};
    int vx[4] = {0, -1, 1, 0};
    for(int i=0;i<4;i++){
        if(!check(x+vx[i], y+vy[i]) || mas[y+vy[i]][x+vx[i]] == 0) continue;
        dfs(mas, x+vx[i], y+vy[i], ct+1);
    }
    mas[y][x] = 1;
    
}

int main(void){
    // Your code here!
    cin>>n>>m;
     
    vector<vector<int>> mas(m, vector<int>(n));
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            cin>>mas[i][j];
        }
    }
    //cout<<mas[0][2]<<endl;
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if(mas[i][j]==1){
                dfs(mas, j, i, 1);
            }
        }
    }
    
    
    cout<<ans<<endl;
}
