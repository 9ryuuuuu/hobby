n = int(input())
A = [int(i) for i in input().split()]
q = int(input())
M = [int(i) for i in input().split()]


def set_possible_m(depth: int, sum: int):
    possible_m[sum] = True

    if depth == n:
        return

    set_possible_m(depth + 1, sum)
    if sum + A[depth] < 2000:
        set_possible_m(depth + 1, sum + A[depth])


possible_m = [False] * 2000
set_possible_m(0, 0)

for mi in M:
    if possible_m[mi]:
        print('yes')
    else:
        print('no')

