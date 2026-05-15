#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector <int>a;
    int count=1000000000;
    int n=0;
    while(n<count){
        for(int i=2;i<(n/2)+1;i++){
            if(n%i==0){
                a.push_back(n);
                break;
            }
        }
        n+=1;
    }
    cout<<a
}