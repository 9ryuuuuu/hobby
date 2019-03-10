num = int(input())
for i in range(1, num + 1):
    if i % 3 == 0:
        print(f' {i}', end='')
    else:
        x = i
        while x:
            if x % 10 == 3:
                print(f' {i}', end='')
                break
            x //= 10  # 切り捨て除算
print()