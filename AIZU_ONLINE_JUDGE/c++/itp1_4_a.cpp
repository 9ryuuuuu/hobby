#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;
    cout << int(a / b) << " " << a % b << " ";
    cout << fixed;
    cout << setprecision(10) << double(a) / double(b) << endl;
}
