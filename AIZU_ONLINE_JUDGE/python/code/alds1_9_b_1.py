import sys
import math

from typing import List


def max_heapify(array: List[int], ix: int) -> None:
    l_ix = ix * 2
    r_ix = ix * 2 + 1

    # 左の子、自分、右の子の中で値が最大のノードを選ぶ。
    if l_ix < len(array) and array[l_ix] > array[ix]:
        largest_ix = l_ix
    else:
        largest_ix = ix
    if r_ix < len(array) and array[r_ix] > array[largest_ix]:
        largest_ix = r_ix

    # 自分より子の方が大きい場合、自分と子を入れ替えて、再度max_heapifyを呼ぶ。
    if largest_ix != ix:
        array[ix], array[largest_ix] = array[largest_ix], array[ix]
        max_heapify(array, largest_ix)


def build_max_heap(array: List[int]) -> List[int]:
    """真ん中のインデックスから降順にmax_heapfyを適用することで、max_heapを構築する。"""
    half = math.floor(len(array) / 2)
    for i in reversed(range(1, half + 1)):
        max_heapify(array, i)
    return array


_n = int(input())
array = [int(i) for i in input().split()]
# arrayのindexを1から開始する。
array.insert(0, sys.maxsize)
max_heap = build_max_heap(array)
for val in max_heap[1:]:
    print(f' {val}', end='')
print()
