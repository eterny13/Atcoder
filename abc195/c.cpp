#include <bits/stdc++.h>
using namespace std;

int main(void){
  long long n, cnt=0;
  cin>>n;

  if(n>=1e3) cnt  += n - 999;
  if(n>=1e6) cnt  += n - 999999;
  if(n>=1e9) cnt  += n - 999999999;
  if(n>=1e12) cnt += n - 999999999999;
  if(n>=1e15) cnt += n - 99999999999999;

  cout << cnt << endl;
  
}

