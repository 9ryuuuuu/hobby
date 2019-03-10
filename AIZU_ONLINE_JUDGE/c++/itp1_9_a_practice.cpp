#include <iostream>
#include <string>
using namespace std;

int main()
{
    // Example1

    // int n;
    // string greeting = "HellO";
    // cout << (greeting == "hello") << endl;
    // greeting[0] = 'h';
    // greeting[greeting.size() - 1] = 'o';
    // cout << (greeting == "hello") << endl;

    // Example2

    int n;
    string color = "black";
    color = "white";
    cout << "0: " << color << endl;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cin >> color;
        cout << i << ": " << color << endl;
    }
    return 0;
}
