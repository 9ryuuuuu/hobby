import math

n = int(input())  # リストAの要素数
A = [int(input()) for i in range(n)]


def get_G(n):
    """シェルソートの間隔を格納した配列を返す。

    Args:
        n ([type]): ソート対象の配列の要素数。

    Returns:
        [type]: シェルソートの間隔を格納した配列
    """
    ret_list = []
    tmp = math.floor(n / 2)
    ret_list.append(tmp)
    while tmp > 1:
        tmp = math.floor(tmp / 2)
        ret_list.append(tmp)
    return ret_list


def insertion_sort(A, n, g):
    """[summary]

    Args:
        A ([type]): ソート対象の配列
        n ([type]): Aの要素数
        g ([type]): シェルソートの間隔
    """
    global cnt
    for i in range(g, n):
        tmp = A[i]
        j = i - g
        while j >= 0 and A[j] > tmp:
            A[j + g] = A[j]
            j = j - g
            cnt += 1
        A[j + g] = tmp


def shell_sort(A, n):
    global cnt
    for g in G:
        insertion_sort(A, n, g)


# G = [4, 2, 1]
G = get_G(n)
cnt = 0

shell_sort(A, n)
print(len(G))
print(' '.join(map(str, G)))
print(cnt)
for a in A:
    print(a)