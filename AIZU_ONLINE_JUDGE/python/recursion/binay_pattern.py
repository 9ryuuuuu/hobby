"""0か1かのパターンを格納したリストを作成する。"""

from typing import List


def rec(pattern: List[int], index: int, length: int, ret_list: List[int]):
    """0か1かの組み合わせを作成する。"""

    if index >= length:
        # print(pattern)
        ret_list.append([i for i in pattern])
        return
    for i in range(2):
        pattern[index] = i
        rec(pattern, index + 1, length, ret_list)


def get_bainary_pattern_list(length: int) -> List[int]:
    """0か1かの全パターンを格納したリストを作成する。"""
    ret_list = []
    binary_pattern = [-1 for i in range(length)]
    rec(binary_pattern, 0, length, ret_list)
    return ret_list


binary_pattern_list = get_bainary_pattern_list(3)
for b in binary_pattern_list:
    print(b)