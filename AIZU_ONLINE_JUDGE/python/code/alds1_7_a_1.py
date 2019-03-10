from typing import List

# id
# k 子の数
# 子のID


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


class Node(sort_object):

    node_id = -999
    child = []
    parent = -1
    depth = -999
    node_type = 'Not set'

    def __init__(self, id: int, child: List[int]):
        self.node_id = id
        self.child = child

    def show(self):
        out = f'node {self.node_id}: '
        out += f'parent = {self.parent}, depth = {self.depth}, '
        out += f'{self.node_type}, '
        tmp = ', '.join(map(str, self.child))
        out += f'[{tmp}]'
        print(out)

    def get_value(self):
        return self.node_id


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


def debug(node_list: List[Node]):
    for n in node_list:
        n.show()


def get_parent(node_id: int) -> int:
    for n in node_list:
        if n.node_id == node_id:
            return n.parent


def get_depth(depth: int, node_id: int) -> int:
    parent = get_parent(node_id)
    if parent != -1:
        depth += 1
        return get_depth(depth, parent)
    return depth


def set_node_info(node_list: List[Node]):
    # 親を設定する。
    for target in node_list:
        for search in node_list:
            if target.node_id in search.child:
                target.parent = search.node_id

    # depthを設定する。
    for target in node_list:
        depth = get_depth(0, target.node_id)
        target.depth = depth

    # typeを設定する。
    for target in node_list:
        if target.depth == 0:
            target.node_type = 'root'
        elif target.depth > 0:
            target.node_type = \
                'leaf' if len(target.child) == 0 else 'internal node'
        else:
            raise ValueError()


n = int(input())
node_list = []
for _i in range(n):
    line = [int(i) for i in input().split()]
    node_id = line[0]
    if line[1] >= 1:
        child = line[2:]
    else:
        child = []
    node_list.append(Node(node_id, child))

set_node_info(node_list)
QuickSort.quick_sort(node_list, 0, n - 1)
debug(node_list)

