"""安定かどうかを確認する処理で時間オーバーになる。。"""

from typing import List, Tuple


def partition(A: List[Tuple[str, int]], p: int, r: int) -> int:
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
    tmp = A[r][1]
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= tmp:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort(A: List[Tuple[str, int]], p: int, r: int) -> None:
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)
    return


def is_stable(original, after):
    """安定かどうかを確認する。

    O(n^4)のオーダーのため、時間オーバーになる。

    Args:
        original ([type]): [description]
        after ([type]): [description]

    Returns:
        [type]: [description]
    """

    for i in range(len(original) - 1):
        for j in range(i + 1, len(original)):
            for a in range(len(original) - 1):
                for b in range(a + 1, len(original)):
                    if original[i][1] == original[j][1] \
                       and original[i] == after[b] \
                       and original[j] == after[a]:
                        return False
    return True


n = int(input())
cards = []
for _i in range(n):
    pic, num = map(str, input().split())
    num = int(num)
    cards.append((pic, num))
original = [i for i in cards]

quick_sort(cards, 0, n - 1)
if is_stable(original, cards):
    print('Stable')
else:
    print('Not stable')
for c in cards:
    print(c[0], c[1])