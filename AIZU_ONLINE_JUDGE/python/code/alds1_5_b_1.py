import sys
from typing import List
import math

n = int(input())
S = [int(i) for i in input().split()]
hikaku = 0


def merge(A: List[int], left: int, mid: int, right: int) -> None:
    global hikaku

    left_list = A[left:mid]
    right_list = A[mid:right]
    left_list.append(sys.maxsize)
    right_list.append(sys.maxsize)

    i = 0  # left_listのインデックス
    j = 0  # right_listのインデックス
    for k in range(left, right):
        hikaku += 1
        if left_list[i] <= right_list[j]:
            A[k] = left_list[i]
            i += 1
        else:
            A[k] = right_list[j]
            j += 1


def merge_sort(A: List[int], left: int, right: int) -> int:
    if left + 1 < right:
        mid = math.floor((left + right) / 2)
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)


merge_sort(S, 0, len(S))
print(' '.join(map(str, S)))
print(hikaku)
