#include <bits/stdc++.h>
using namespace std;
int main(void){
  int n,m;
  cin>>n>>m;

  int ab[m][2];
  for(int i=0;i<m;i++){
    cin>>ab[i][0]>>ab[i][1];
  }

  int k;
  cin>>k;
  int cd[k][2];
  for(int i=0;i<k;i++){
    cin>>cd[i][0]>>cd[i][1];
  }

  int cnt = 0;
  for(int j=0;j<(1<<k);j++){
    int x = j;
    set<int> s;

    for(int i=0;i<k;i++){
      if(((x>>i)&1) == 0){
        s.insert(cd[i][0]);
      }
      else{
        s.insert(cd[i][1]);
      }
    }

    int ct=0;
    for(int ii=0;ii<m;ii++){
      if(s.count(ab[ii][0]) > 0 && s.count(ab[ii][1]) > 0){
        ct++;
      }
    }
    cnt = max(cnt,ct);
  }
  cout<<cnt<<endl;

}


