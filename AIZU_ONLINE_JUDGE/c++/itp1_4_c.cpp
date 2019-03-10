#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int a, b;
    string op;
    while (true)
    {
        cin >> a >> op >> b;
        if (op == "?")
            break;
        if (op == "+")
            cout << a + b << endl;
        if (op == "-")
            cout << a - b << endl;
        if (op == "*")
            cout << a * b << endl;
        if (op == "/")
            cout << a / b << endl;
    }
}