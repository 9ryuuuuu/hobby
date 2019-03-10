"""マージソートの一般的な使用例。"""
# (並べるキーとなる値、それに紐づく要素1、それに紐づく要素2) をマージソートで並び替える。

import sys
from typing import List
import math


class sort_object:
    """ソート対象のオブジェクト。必要に応じてプロパティやメソッドを増やす。"""

    def __init__(self, value: int, inf1='', inf2=''):
        self.value = value
        self.inf1 = inf1

    def set_value(self, value: int):
        self.set_value = value

    def get_value(self):
        return self.value

    def set_inf1(self, inf1):
        self.inf1 = inf1

    def get_inf1(self):
        return self.inf1

    def set_inf2(self, inf2):
        self.inf2 = inf2

    def get_inf2(self):
        return self.inf2


def merge(A: List[sort_object], left: int, mid: int, right: int) -> None:

    left_list = A[left:mid]
    right_list = A[mid:right]
    left_list.append(sort_object(sys.maxsize))
    right_list.append(sort_object(sys.maxsize))

    i = 0  # left_listのインデックス
    j = 0  # right_listのインデックス
    for k in range(left, right):
        if left_list[i].get_value() <= right_list[j].get_value():
            A[k] = left_list[i]
            i += 1
        else:
            A[k] = right_list[j]
            j += 1


def merge_sort(A: List[sort_object], left: int, right: int) -> int:
    """マージソート。

    Args:
        A (List[sort_object]): ソート対象
        left (int): ソート対象の先頭のインデックス
        right (int): ソート対象の最後のインデックス + 1
    """

    if left + 1 < right:
        mid = math.floor((left + right) / 2)
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)


target_list = []
target_list.append(sort_object(90, 'AAA'))
target_list.append(sort_object(87, 'BBB'))
target_list.append(sort_object(3, 'A'))
target_list.append(sort_object(87, 'BBA'))
target_list.append(sort_object(10, 'AC'))
merge_sort(target_list, 0, len(target_list))
for so in reversed(target_list):
    print(so.get_value(), so.get_inf1())
