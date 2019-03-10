"""マージソートを用いて安定かどうかを確認する。"""

import math
import sys
from typing import List


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


class MergeSort:

    @classmethod
    def merge(cls, A: List[sort_object], left: int, mid: int, right: int) -> None:

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

    @classmethod
    def merge_sort(cls, A: List[sort_object], left: int, right: int) -> None:
        """マージソート。

        Args:
            A (List[sort_object]): ソート対象
            left (int): ソート対象の先頭のインデックス
            right (int): ソート対象の最後のインデックス + 1
        """
        if left + 1 < right:
            mid = math.floor((left + right) / 2)
            cls.merge_sort(A, left, mid)
            cls.merge_sort(A, mid, right)
            cls.merge(A, left, mid, right)


class QuickSort:

    @classmethod
    def partition(cls, A: List[sort_object], p: int, r: int) -> int:
        """パーティション

        A[p, ..., r]を、A[p, ..., q-1]とA[q+1, ..., r]二分割する。
        A[p, ..., q-1]の各要素は A[q]以下とする。
        A[q+1, ..., r]の各要素は A[q]より大きくする。

        Args:
            A (List[int]): 分割対象のリスト
            p (int): 分割対象のリストの先頭のインデックス
            r (int): 分割対象のリストの最後のインデックス

        Returns:
            int: q
        """
        tmp = A[r].get_value()
        i = p - 1
        for j in range(p, r):
            if A[j].get_value() <= tmp:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1

    @classmethod
    def quick_sort(cls, A: List[sort_object], p: int, r: int) -> None:
        """[summary]

        Args:
            A (List[sort_object]): ソート対象
            p (int): ソート対象の先頭のインデックス
            r (int): ソート対象の最後のインデックス
        """

        if p < r:
            q = cls.partition(A, p, r)
            cls.quick_sort(A, p, q - 1)
            cls.quick_sort(A, q + 1, r)
        return


target_list = []
target_list.append(sort_object(90, 'AAA'))
target_list.append(sort_object(87, 'BBB'))
target_list.append(sort_object(3, 'A'))
target_list.append(sort_object(87, 'BBA'))
target_list.append(sort_object(10, 'AC'))
target_list_2 = [val for val in target_list]
print('入力値')
for t, t2 in zip(target_list, target_list_2):
    print(t.get_inf1(), t.get_value())
print()

QuickSort.quick_sort(target_list, 0, len(target_list) - 1)
MergeSort.merge_sort(target_list_2, 0, len(target_list_2))

print('ソート結果。')
print('クイックソート(左)は安定なソートでないため、マージソート(右)と結果が異なる。')
for t, t2 in zip(target_list, target_list_2):
    print(t.get_inf1(), t.get_value(), t2.get_inf1(), t2.get_value())
