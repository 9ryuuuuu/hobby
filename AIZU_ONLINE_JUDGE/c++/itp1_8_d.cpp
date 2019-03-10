#include <iostream>
#include <cstring>
#include <stdio.h>
using namespace std;
int main()
{
    char s[100], p[100], ss[200];
    scanf("%s %s", s, p);
    strcpy(ss, s);
    strcat(ss, s);
    if (strstr(ss, p) == NULL)
        printf("No\n");
    else
        printf("Yes\n");
}