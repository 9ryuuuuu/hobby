#include <iostream>
#include <unordered_map>
using namespace std;

int main()
{
    unordered_map<string, int> m = {
        {"foo", 3},
        {"bar", 5},
        {"buz", 10}};

    cout << m["foo"] << endl;
}
