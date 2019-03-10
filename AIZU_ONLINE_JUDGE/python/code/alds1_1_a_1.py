def out(data) -> str:
    print(' '.join(map(str, data)))


N = int(input())
data = [int(i) for i in input().split()]
out(data)
for i in range(1, N):
    tmp = data[i]
    j = i - 1
    while j >= 0 and data[j] > tmp:
        data[j + 1] = data[j]
        j -= 1
    data[j + 1] = tmp
    out(data)