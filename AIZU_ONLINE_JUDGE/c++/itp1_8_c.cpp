#include <iostream>
using namespace std;

int main()
{
    char ch;
    int count[26];

    for (int i = 0; i < 26; i++)
        count[i] = 0;

    while (cin >> ch)
    {
        int small;
        small = tolower(ch);
        int i = small - 'a';
        count[i]++;
    }

    for (int i = 0; i < 26; i++)
    {
        cout << char(i + int('a')) << ' ' << ':' << ' ' << count[i] << endl;
    }
}
