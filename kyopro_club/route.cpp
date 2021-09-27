#include<bits/stdc++.h>
using namespace std;

const int P = 1000000007;

long long frac(long long a, long long n) {
  long long res=1;
  while(n>0) {
    if(n%2 == 1) res=res*a%P;
    a=a*a%P;
    n/=2;
  }
  return res;
}

int main(void){

  int w,h;

  cin>>w>>h;
  w--; h--;

  long long a=1,b=1;
  for(int i=0;i<w;i++)  a=a*(w+h-i)%P;
  for(int i=1;i<=w;i++) b=b*i%P;

  cout<< a * frac(b, P-2)%P << endl;

}
