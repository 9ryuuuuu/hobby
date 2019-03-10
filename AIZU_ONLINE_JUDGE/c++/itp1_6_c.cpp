#include <iostream>
using namespace std;

int main()
{
    int n;
    int b, f, r, v;
    int people[5][4][11];
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            for (int k = 0; k < 11; k++)
            {
                people[i][j][k] = 0;
            }
        }
    }

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> b >> f >> r >> v;
        people[b][f][r] += v;
    }

    for (int i = 1; i < 5; i++)
    {
        for (int j = 1; j < 4; j++)
        {
            for (int k = 1; k < 11; k++)
            {
                cout << " " << people[i][j][k];
            }
            cout << endl;
        }
        if (i < 4)
        {
            cout << "####################" << endl;
        }
    }
}
