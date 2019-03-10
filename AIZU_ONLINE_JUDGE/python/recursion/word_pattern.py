""""文字の総パターンを作成する。"""

from typing import List


def make_word_pattern(word_pattern: List[int], ret_list: List[str],
                      candidate_words: List[str], number_of_digits: int):
    """文字の組み合わせを作成する。"""
    if len(word_pattern) >= number_of_digits:
        # print(word_pattern)
        ret_list.append(word_pattern)
        return
    for candidate_word in candidate_words:
        make_word_pattern(word_pattern + candidate_word, ret_list,
                          candidate_words, number_of_digits)


def get_word_pattern_list(candidate_words: List[str],
                          number_of_digits: int) -> List[str]:
    """文字の組み合わせの総パターンを格納したリストを作成する。"""
    candidate_words = ['A', 'B', 'C', 'D']
    number_of_digits = 6
    word_pattern = ''
    ret_list = []
    make_word_pattern(word_pattern, ret_list, candidate_words,
                      number_of_digits)
    return ret_list


word_pattern_list = get_word_pattern_list()
print(len(word_pattern_list))
# for w in word_pattern_list:
#     print(w, end=' ')