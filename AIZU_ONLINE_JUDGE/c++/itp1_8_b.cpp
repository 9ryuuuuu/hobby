#include <iostream>
using namespace std;
int main()
{
    string number = "";
    while (true)
    {
        cin >> number;
        if (number == "0")
            break;
        int sum = 0;
        for (int i = 0; i < number.size(); i++)
        {
            // 以下の処理はすべて等価
            sum += number[i] - '0';
            // sum += int(number[i]) - 48;
            // sum += int(number[i]) - int('0');
        }
        cout << sum << endl;
    }
}