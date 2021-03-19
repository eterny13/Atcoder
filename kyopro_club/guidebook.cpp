#include <bits/stdc++.h>
using namespace std;

int main(void) {
  int n;
  cin>>n;
  vector<pair<pair<string,int>,int> > p(n);

  for(int i=0;i<n;i++){
    string s;
    int pt;
    cin>>s>>pt;
    p[i] = make_pair(make_pair(s, -pt), i+1);
  }
  sort(p.begin(),p.end());
  for(int i=0;i<n;i++) {
    cout << p[i].second << endl;
  }
}