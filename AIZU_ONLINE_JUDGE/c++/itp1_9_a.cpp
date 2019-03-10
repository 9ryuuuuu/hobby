#include <iostream>
#include <string>
using namespace std;

int main()
{
    string t;
    string w;
    int cnt = 0;

    cin >> w;
    for (int i = 0; i < w.size(); i++)
    {
        if ('A' <= w[i] && w[i] <= 'Z')
            w[i] += 'a' - 'A';
    }

    cin >> t;
    while (t != "END_OF_TEXT")
    {
        for (int i = 0; i < t.size(); i++)
            if ('A' <= t[i] && t[i] <= 'Z')
                t[i] += 'a' - 'A';
        if (w == t)
            cnt++;
        cin >> t;
    }
    cout << cnt << endl;
}
