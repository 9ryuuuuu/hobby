"""高速化version

それまでに調べたRの中で最小のものを保持することで計算量を減らす。
"""

N = int(input())
R = [int(input()) for i in range(N)]

min_v = R[0]
max_v = R[1] - R[0]
for i in range(1, len(R)):
    if min_v > R[i - 1]:
        min_v = R[i - 1]
    if max_v < R[i] - min_v:
        max_v = R[i] - min_v
print(max_v)