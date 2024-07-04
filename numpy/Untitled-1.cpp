// #include<iostream>
// #include<vector>
// using namespace std;
//   int valueAfterKSeconds(int n, int k) {
//         int s=0;
//         int x=0;
//         int sum=0;
//         vector<int> ans;
//         for(int i=0;i<n;i++){
//             ans.push_back(1);
//         }

//         while(s<k){
//             x=0;
//             while(x<ans.size()){
//                 sum=ans[x]+ans[x+1];
//                 ans[x+1]=sum;
//                 x++;
//             }
//             s++;

            
//         }
//         return ans[ans.size()];
        
//     }
//     int main(){
//         cout<<valueAfterKSeconds(7,5);
//         cout<<"hello";

//     }


#include <cmath>
#include <cstdio>
#include <vector>
#include<string>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    string s;
    cin>>n;
    cin>>s;
    vector<int> vec ;
    for( int i=0;i<s.size();i++){
        if(s[i] != " "){
            vec.push_back(s[i]);
        }
    }
    
    for(int i=0;i<vec.size();i++){
        cout<<vec[i];
    }
    
    
    return 0;
}