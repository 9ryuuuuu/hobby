#include <iostream>
using namespace std;

void arr_1();
void arr_2();
void arr_3();
int main()
{

    // arr_1();
    // arr_2();
    arr_3();
}

void arr_3()
{

    int n = 3;
    int ***arr = new int **[n];
    for (int i = 0; i < n; i++)
    {
        arr[i] = new int *[n];
        for (int j = 0; j < n; j++)
        {
            arr[i][j] = new int[n];
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            for (int k = 0; k < n; k++)
            {
                arr[i][j][k] = i * 100 + j * 10 + k;
                cout << arr[i][j][k] << endl;
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            delete[] arr[i][j];
        }
        delete[] arr[i];
    }
    delete[] arr;
}

void arr_2()
{
    int n = 3;
    int **arr = new int *[n];
    for (int i = 0; i < n; i++)
    {
        arr[i] = new int[n];
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            arr[i][j] = i * 10 + j;
            cout << arr[i][j] << endl;
        }
    }

    for (int i = 0; i < n; i++)
    {
        delete[] arr[i];
    }
    delete[] arr;
}

void arr_1()
{
    int n = 10;
    int *arr;
    arr = new int[n];
    for (int i = 0; i < n; i++)
    {
        arr[i] = i;
        cout << arr[i] << endl;
    }

    delete[] arr;
}
