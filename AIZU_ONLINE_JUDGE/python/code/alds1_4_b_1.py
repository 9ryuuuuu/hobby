from typing import List
import math

N = int(input())
S = [int(i) for i in input().split()]
q = int(input())
T = [int(i) for i in input().split()]


def binary_search(A: List[int], key: int) -> int:
    left = 0
    right = len(A)
    while left < right:
        mid = math.floor((left + right) / 2)
        if A[mid] == key:
            return mid
        elif key < A[mid]:
            right = mid
        else:
            left = mid + 1
    return -1


count = 0
for t in T:
    if binary_search(S, t) != -1:
        count += 1
print(count)