#include <iostream>
using namespace std;

int main()
{
    int n, m;
    int A[100][100];
    int b[100];

    cin >> n >> m;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> A[i][j];
        }
    }
    for (int i = 0; i < m; i++)
    {
        cin >> b[i];
    }

    for (int i = 0; i < n; i++)
    {
        int tmp = 0;
        for (int j = 0; j < m; j++)
        {
            tmp += A[i][j] * b[j];
        }
        cout << tmp << endl;
    }
}
