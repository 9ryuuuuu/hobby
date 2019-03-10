#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int n, val;
    long long min = 1000000, max = -1000000, sum = 0;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> val;
        if (val < min)
            min = val;
        if (val > max)
            max = val;
        sum += val;
    }
    cout << min << " " << max << " " << sum << endl;
}