from typing import List


def partition(A: List[int], p: int, r: int) -> int:
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
    tmp = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= tmp:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


n = int(input())
A = [int(i) for i in input().split()]
q = partition(A, 0, n - 1)
result = [str(A[i]) if i != q else '[' + str(A[i]) + ']' for i in range(len(A))]
print(' '.join(result))
