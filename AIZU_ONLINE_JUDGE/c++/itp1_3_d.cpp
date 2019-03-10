#include <iostream>
using namespace std;

int main()
{
    int a, b, c;
    int cnt;
    cin >> a >> b >> c;
    for (int i = a; i <= b; i++)if (c%i==0) cnt++;
    cout << cnt << endl;
}
