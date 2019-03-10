"""素数を求める。

以下の性質を用いる。
合成数 x は p <= sqrt(x) を満たす素因子 pをもつ。
"""

import math


def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    for i in range(3, math.floor(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


N = int(input())
data = [int(input()) for i in range(N)]
cnt = 0
for d in data:
    if is_prime(d):
        cnt += 1
print(cnt)
