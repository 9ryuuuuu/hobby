import sys
from typing import List
import math


def merge(A: List[int], left: int, mid: int, right: int) -> None:

    left_list = A[left:mid]
    right_list = A[mid:right]
    left_list.append(sys.maxsize)
    right_list.append(sys.maxsize)

    i = 0  # left_listのインデックス
    j = 0  # right_listのインデックス
    for k in range(left, right):
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


target_list = [63, 16, 24, 7, 29, 57, 65, 26, 36, 32, 50, 5, 34, 1, 18, 15, 49, 9, 47, 53, 10, 35, 76, 79]
merge_sort(target_list, 0, len(target_list))
print(target_list)