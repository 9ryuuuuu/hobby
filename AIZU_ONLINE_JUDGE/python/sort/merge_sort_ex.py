import sys
from typing import List
import math


def merge(A: List[List], left: int, mid: int, right: int) -> None:

    left_list = A[left:mid]
    right_list = A[mid:right]
    left_list.append((sys.maxsize, '---'))
    right_list.append((sys.maxsize, '---'))

    i = 0  # left_listのインデックス
    j = 0  # right_listのインデックス
    for k in range(left, right):
        if left_list[i][0] <= right_list[j][0]:
            A[k] = left_list[i]
            i += 1
        else:
            A[k] = right_list[j]
            j += 1


def merge_sort(A: List[List], left: int, right: int) -> int:
    if left + 1 < right:
        mid = math.floor((left + right) / 2)
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)


target_list = []
target_list.append((90, 'AAA'))
target_list.append((87, 'BBB'))
target_list.append((3, 'A'))
target_list.append((87, 'BBA'))
target_list.append((10, 'AC'))
merge_sort(target_list, 0, len(target_list))
print(target_list)