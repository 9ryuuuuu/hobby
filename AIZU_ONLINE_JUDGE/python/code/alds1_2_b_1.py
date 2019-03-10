from typing import List


def selection_sort(A: List[int]) -> int:
    cnt = 0
    for i in range(len(A)):
        min_j = i
        for j in range(i, len(A)):
            if A[j] < A[min_j]:
                min_j = j
        if min_j != i:
            cnt += 1
        A[i], A[min_j] = A[min_j], A[i]
    return cnt


N = int(input())
A = [int(i) for i in input().split()]
cnt = selection_sort(A)
print(' '.join(map(str, A)))
print(cnt)