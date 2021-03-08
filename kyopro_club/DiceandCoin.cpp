#include <bits/stdc++.h>
using namespace std;

int main(void) {
  int n,k;
  cin>>n>>k;

  double ans = 0;
  for(int i=1;i<=n;i++){
    int x = i;
    int cnt = 0;
    while(x < k){
      x = x*2;
      cnt++;
    }
    ans += 1.0 / n * pow(0.5, cnt);
  }

  printf("%.12f\n", ans);
}