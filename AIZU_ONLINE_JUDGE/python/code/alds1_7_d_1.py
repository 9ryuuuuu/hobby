
# preorder tree walk(先行順巡回)
# inorder tree walk(中間順巡回)
# 1. inorderの性質:
# inorderは左部分木、節点、右部分木の順で回るため、節点を区切りに左部分木、右部分木に分かれる。
# 2. preorderの性質:
# preorderは節点、左部分木、右部分木の順で回るため、節点を先に回る。
# 1 より、inorderを左部分木、右部分木に分割することを再帰的に行えばよい。
# そのためには、inorderを左部分木と右部分木に分割する根を見つける必要がある。
# 2 より、inorderと一致する要素の中で、preorderで最初に出てくるのが根である。
# 参考: http://ikapblg.blog.fc2.com/blog-entry-56.html


class Node:
    left = -1
    right = -1


def get_root_index(first: int, end: int) -> int:
    """inorder[first:end]の根のインデックスを取得する。
    根： inorder[first:end]を左部分木と右部分木に分割するノード
    """

    # inorder[first:end]の要素でpreorderの一番手前にあるものが、
    # inorder[first:end]を左部分木と右部分木に分割するノードなので、
    # そのインデックスを返す。
    for pre in preorder:
        for j in range(first, end):
            if pre == inorder[j]:
                return j


def get_root(first, end) -> int:
    """inorder[first:end]の根のノードを返す。
    ないときは、-1を返す。
    """
    if first < end:
        return inorder[get_root_index(first, end)]
    else:
        return -1


def set_nodes(first: int, end: int):
    """ノードの関係を設定する。

    inorder[first:end]における根を見つけ、
    その根に左ノード、右ノードを登録することを再帰的に繰り返す。

    Args:
        first (int): inorderにおける対象範囲の左端のインデックス
        end (int): inorderにおける対象範囲の右端+1のインデックス
    """

    root_ix = get_root_index(first, end)
    if first + 1 < root_ix:
        set_nodes(first, root_ix)
    if root_ix + 1 < end - 1:
        set_nodes(root_ix + 1, end)
    nodes[inorder[root_ix]].left = get_root(first, root_ix)
    nodes[inorder[root_ix]].right = get_root(root_ix + 1, end)


def set_postorder(node_id: int) -> None:
    """後行順巡回で得られる節の番号を保存する。"""

    left = nodes[node_id].left
    if left != -1:
        set_postorder(left)

    right = nodes[node_id].right
    if right != -1:
        set_postorder(right)

    postorder.append(node_id)


N = int(input())
nodes = [Node() for i in range(N + 1)]
preorder = [int(i) for i in input().split()]
inorder = [int(i) for i in input().split()]

set_nodes(0, N)

postorder = []
set_postorder(get_root(0, N))
print(' '.join(map(str, postorder)))