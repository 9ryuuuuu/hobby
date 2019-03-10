while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for i in range(H):
        aaa = i % 2  # iが偶数なら0。奇数なら1。
        for j in range(W):
            if j % 2 == aaa:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()