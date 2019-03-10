#include <iostream>
// #include <cmath>
using namespace std;

int main(){
    int n, h;
    cin >> n;
    cout << int(n /3600) << ":" << (n % 3600)/60 << ":" << (n % 3600)%60 << endl;
}