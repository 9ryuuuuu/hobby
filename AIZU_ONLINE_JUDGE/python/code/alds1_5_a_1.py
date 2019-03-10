from typing import List

n = int(input())
A = [int(i) for i in input().split()]
# A = [int(i) for i in '1 5 7 10 21'.split()]
q = int(input())
M = [int(i) for i in input().split()]
# M = [int(i) for i in '2 4 17 8'.split()]


def solve(value: int, depth: int):
    if value == 0:
        return True
    if depth >= n:
        return False
    res = solve(value, depth + 1) | solve(value - A[depth], depth + 1)
    return res


for mi in M:
    if solve(mi, 0):
        print('yes')
    else:
        print('no')

