from typing import List


def bublle_sort(A: List[int]) -> List[int]:
    cnt = 0
    flg = True
    while flg:
        flg = False
        for i in reversed(range(1, N)):
            if A[i] < A[i - 1]:
                A[i], A[i - 1] = A[i - 1], A[i]
                cnt += 1
                flg = True
    return A, cnt


N = int(input())
A = [int(i) for i in input().split()]
A, cnt = bublle_sort(A)
print(' '.join(map(str, A)))
print(cnt)
