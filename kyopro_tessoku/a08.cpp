#include <bits/stdc++.h>
using namespace std;
int main(void){
    // Your code here!
    int h,w,q;
    cin>>h>>w;
    vector<vector<int>> board(h, vector<int> (w,0));
    vector<vector<int>> acc(h+1, vector<int> (w+1,0));
    
    for(int i=0;i<h;i++) {
        for(int j=0;j<w;j++) {
            cin>>board[i][j];
        }
    }
    for(int i=1;i<=h;i++) {
        for(int j=1;j<=w;j++) {
            acc[i][j] = board[i-1][j-1] + (acc[i][j-1] - acc[i-1][j-1]) + acc[i-1][j];
            //cout << acc[i][j] << " ";
        }
        //cout << endl;
    }
    
    cin>>q;
    for(int i=0;i<q;i++) {
        int a,b,c,d;
        cin>>a>>b>>c>>d;
        cout << acc[c][d] - acc[a-1][d] - acc[c][b-1] + acc[a-1][b-1] << endl;
    }
}
