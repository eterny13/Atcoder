#include <bits/stdc++.h>
using namespace std;

int main(void){
  int n;
  cin>>n;

  vector<int> A(n);
  vector<vector<int> > dp(n+1, vector<int> (n+1,0));
  int l = 0;
  for(int i=0;i<n;i++){
    int t;
    cin>>t;

    if(i == 0){
      A[0] = t;
    }
    else{
      if(A[l] < t){
        l++;
        A[l] = t;
      }
      else {
        for(int j=0;j<=l;j++){
          if(A[j] >= t){
            A[j] = t;
            break;
          }
        }
      }
    }
  }

  cout << l + 1 << endl;

}