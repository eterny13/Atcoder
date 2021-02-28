#include <bits/stdc++.h>
using namespace std;

int main(void){
  long long n;
  cin>>n;

  set<long long> s;
  for(long long i=2; i*i<=n;i++){
    long long x = i*i;
    while(x <= n){
      s.insert(x);
      x *= i;
    }
  }

  cout<<n-s.size()<<endl;
}

