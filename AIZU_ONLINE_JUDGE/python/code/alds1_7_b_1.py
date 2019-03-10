from typing import List


class Node:
    parent = -1  # 親。親を持たない場合は-1
    sibling = -1  # 兄弟。兄弟を持たない場合は、-1
    degree = -99  # 子の数
    depth = -99  # 深さ
    height = -99  # 高さ
    node_type = 'Not set'  # 根(root)、内部節点(internal node)、葉(leaf)
    left = -99
    right = -99


num_of_node = int(input())
nodes = [Node() for i in range(num_of_node)]
for _i in range(num_of_node):
    node_id, left, right = map(int, input().split())
    # 子を持たない場合は、leftやrightは-1
    nodes[node_id].left = left
    nodes[node_id].right = right

    degree = 0
    if left != -1:
        degree += 1
    if right != -1:
        degree += 1
    nodes[node_id].degree = degree

# 親を設定
for i in range(num_of_node):
    if nodes[i].left != -1:
        nodes[nodes[i].left].parent = i
    if nodes[i].right != -1:
        nodes[nodes[i].right].parent = i

# 兄弟を設定
for i in range(num_of_node):
    if nodes[i].parent == -1:
        continue
    # 自分が左の場合
    if nodes[nodes[i].parent].left == i and nodes[nodes[i].parent].right != -1:
        nodes[i].sibling = nodes[nodes[i].parent].right
    # 自分が右の場合
    if nodes[nodes[i].parent].right == i and nodes[nodes[i].parent].left != -1:
        nodes[i].sibling = nodes[nodes[i].parent].left


def set_depth(node_id: int, depth: int):
    nodes[node_id].depth = depth
    if nodes[node_id].left != -1:
        set_depth(nodes[node_id].left, depth + 1)
    if nodes[node_id].right != -1:
        set_depth(nodes[node_id].right, depth + 1)


# 深さを設定
for i in range(num_of_node):
    if nodes[i].parent == -1:
        set_depth(i, 0)
        break


def set_height(node_id: int, height: int):
    if nodes[node_id].height < height:
        nodes[node_id].height = height
    if nodes[node_id].parent != -1:
        set_height(nodes[node_id].parent, height + 1)


# 高さを設定
for i in range(num_of_node):
    if nodes[i].degree == 0:
        set_height(i, 0)

# タイプを設定
for i in range(num_of_node):
    if nodes[i].parent == -1:
        nodes[i].node_type = 'root'
    elif nodes[i].degree != 0:
        nodes[i].node_type = 'internal node'
    else:
        nodes[i].node_type = 'leaf'


for i in range(num_of_node):
    out = f'node {i}: parent = {nodes[i].parent}, sibling = {nodes[i].sibling}'
    out += f', degree = {nodes[i].degree}, depth = {nodes[i].depth}'
    out += f', height = {nodes[i].height}, {nodes[i].node_type}'
    print(out)
