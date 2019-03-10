# N = int(input())
# cards = []
# for i in range(N):
#     line = input().split()
#     a = line[0]
#     num = int(line[1])
#     cards.append((a, num))

suits = ['S', 'H', 'C', 'D']
table = [[False] * 14 for i in range(4)]

with open('input_itp1_6_b_1.txt', mode='r', encoding='utf8') as f:
    N = int(next(f))
    for _i in range(N):
        mark, num = next(f).split()
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