#include <iostream>
#include <iomanip>
#define PI 3.141592653589
using namespace std;

int main()
{
    double r;
    cin >> r;
    cout << setprecision(20) << r * r * PI << " ";
    cout << setprecision(20) << 2 * r * PI << endl;
}