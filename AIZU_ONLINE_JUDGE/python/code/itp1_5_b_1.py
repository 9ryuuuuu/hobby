while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for i, h in enumerate((range(H - 1))):
        if i == 0:
            print('#' * W)
        else:
            print('#' + '.' * (W - 2) + '#')
    print('#' * W)
    print()