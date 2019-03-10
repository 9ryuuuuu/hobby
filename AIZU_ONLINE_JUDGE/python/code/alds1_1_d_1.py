"""タイムリミットになる回答
"""

N = int(input())
R = [int(input()) for i in range(N)]

sa = R[N - 1] - R[N - 2]
for i in reversed(range(N)):
    for j in reversed(range(i)):
        tmp = R[i] - R[j]
        if tmp > sa:
            sa = tmp
print(sa)