suits = ['S', 'H', 'C', 'D']
table = [[False] * 14 for i in range(4)]

N = int(input())
for _i in range(N):
    mark, num = input().split()
    num = int(num)

    if mark == 'S':
        table[0][num] = True
    if mark == 'H':
        table[1][num] = True
    if mark == 'C':
        table[2][num] = True
    if mark == 'D':
        table[3][num] = True

for i in range(4):
    for j in range(1, 14):
        if not table[i][j]:
            print(f'{suits[i]} {j}')