#include <iostream>
#include <map>
using namespace std;

int main()
{
    int n = 0;
    int ar[4][14];
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 14; j++)
            ar[i][j] = 0;

    map<string, int> m;
    m["S"] = 0;
    m["H"] = 1;
    m["C"] = 2;
    m["D"] = 3;

    map<int, string> int2suit;
    int2suit[0] = "S";
    int2suit[1] = "H";
    int2suit[2] = "C";
    int2suit[3] = "D";

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        string suit = "";
        int num;
        cin >> suit >> num;
        ar[m[suit]][num] = 1;
    }
    for (int i = 0; i < 4; i++)
    {
        for (int j = 1; j < 14; j++)
        {
            if (ar[i][j] == 0)
                cout << int2suit[i] << " " << j << endl;
        }
    }
}