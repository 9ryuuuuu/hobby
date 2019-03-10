num = int(input())
for i in range(1, num + 1):
    if i % 3 == 0:
        print(f' {i}', end='')
        continue
    x = i
    while True:
        if x % 10 == 3:
            print(f' {i}', end='')
            break
        x = int(x / 10)
        if x < 1:
            break
print()