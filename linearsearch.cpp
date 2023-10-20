#include<iostream>
using namespace std;
int main(){
    int a[]={1,2,3,4,5};
    int n=sizeof(a)/sizeof(int);
    int key=4,i;
    for(int i=0;i<n;i++)
    {
        if(a[i]==key){
            cout<<"Key found:"<<i<<endl;
            break;
        }
    }
    if(i==n){
        cout<<"Not found";
    }
    return 0;

}