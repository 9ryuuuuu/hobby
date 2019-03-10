from typing import List


class Node:
    left = -1
    right = -1
    parent = -1


def get_root(nodes: List[int]) -> int:
    for i, node in enumerate(nodes):
        if node.parent == -1:
            return i


# TODO
def set_lefts_leaf(nodes: List[int], lefts: List[int], node: int):
    left = nodes[node].left
    parent = nodes[node].parent
    if left == -1:
        if node == nodes[parent].left:
            lefts.append(node)
    else:
        set_lefts_leaf(nodes, lefts, left)

    right = nodes[node].right
    if right != -1:
        set_lefts_leaf(nodes, lefts, right)


def show_preorder(root: int)-> None:
    print(root, end=' ')
    if nodes[root].left != -1:
        show_preorder(nodes[root].left)
    if nodes[root].right != -1:
        show_preorder(nodes[root].right)


def show_inorder(left: int)-> None:
    parent = nodes[left].parent
    if parent != -1 and nodes[parent].right != left:
        print(parent, end=' ')
    if nodes[parent].right != -1 and nodes[nodes[parent].right].left == -1:
        print(nodes[parent].right, end=' ')
    if parent != -1:
        show_inorder(parent)


def show_postorder(left: int)-> None:
    parent = nodes[left].parent
    sibling = nodes[parent].right
    if sibling != -1 and sibling != left:
        print(sibling, end=' ')
    if parent != -1:
        print(parent, end=' ')
    if parent != -1 and nodes[nodes[nodes[parent].parent].right].left == -1:
        show_postorder(parent)
    if parent != -1 and nodes[nodes[parent].parent].right == parent:
        show_postorder(parent)


N = int(input())
nodes = [Node() for i in range(N)]
for _i in range(N):
    node_id, left, right = map(int, input().split())
    nodes[node_id].left = left
    nodes[node_id].right = right
    if left != -1:
        nodes[left].parent = node_id
    if right != -1:
        nodes[right].parent = node_id

print('debug')
for i in range(N):
    print(i, nodes[i].left, nodes[i].right, nodes[i].parent)

root = get_root(nodes)
print(root)
lefts = []
set_lefts_leaf(nodes, lefts, root)
print(lefts)

print('Preorder')
show_preorder(root)
print()

print('Inorder')
for left in lefts:
    print(left, end=' ')
    show_inorder(left)
print()

print('Postorder')
for left in lefts:
    print(left, end=' ')
    show_postorder(left)
print()
