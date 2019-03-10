while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    cnt = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            for k in range(1, n + 1):
                if i == k or j == k:
                    continue
                if (i + j + k) == x:
                    cnt += 1
    print('%d' % (cnt / 6))
