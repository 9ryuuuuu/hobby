from typing import List


def counting_sort(target: List[int], max_val: int) -> List[int]:
    """[summary]

    Args:
        target (List[int]): ソート対象の配列
        max_val (int): ソートする要素の最大値

    Returns:
        List[int]: ソート後の配列
    """
    result = [-1 for i in range(len(target) + 1)]

    # indexがtargetに格納される値に相当するリスト
    counta = [0 for i in range(max_val + 1)]

    # counta[i]にtの出現数を記録する。
    for t in target:
        counta[t] += 1

    # counta[i]にi以下の数の出現数を記録する。
    for i in range(1, max_val + 1):
        counta[i] += counta[i - 1]

    for t in reversed(target):
        result[counta[t]] = t
        counta[t] -= 1

    return result


n = int(input())
target = [int(i) for i in input().split()]
result = counting_sort(target, max(target))

print(' '.join(map(str, result[1:])))

