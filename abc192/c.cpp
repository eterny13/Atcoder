#include <bits/stdc++.h>
using namespace std;
int main(void){

  int n,k;
  cin>>n>>k;

  for(int i=1;i<=k;i++){
    vector<int> num;
    int k = n;
    while(k > 0){
      int s = k%10;
      num.push_back(s);
      k/=10;
    }
    sort(num.begin(), num.end());
    int minv=0;
    for(int i=0;i<num.size();i++){
      minv += num[i]*pow(10.0,i);
    }
    sort(num.begin(), num.end(), greater<int>());
    int maxv=0;
    for(int i=0;i<num.size();i++){
      maxv += num[i]*pow(10.0,i);
    }
    n = abs(maxv - minv);
  }

  cout<<n<<endl;
}


