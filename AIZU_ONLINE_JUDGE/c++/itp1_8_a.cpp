#include <iostream>
#include <cctype>
using namespace std;

int main()
{
    string str;
    getline(cin, str);
    for (int i = 0; i < str.length(); i++)
    {
        if (!isalpha(str[i]))
        {
            cout << str[i];
        }
        else if (islower(str[i]))
        {
            cout << char(toupper(str[i]));
        }
        else
        {
            cout << char(tolower(str[i]));
        }
    }
    cout << endl;
}
