n = int(input())

MAX = 45
table = [0] * MAX
for i in range(MAX):
    # print(n)
    if i == 0 or i == 1:
        table[i] = 1
    else:
        table[i] = table[i - 1] + table[i - 2]

print(table[n])