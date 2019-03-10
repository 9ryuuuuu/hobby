
class Node:

    def __init__(self, key: int) -> None:
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


def input_line() -> (str, int):
    line = input().split()
    if line[0] == 'print':
        return line[0], None
    else:
        return line[0], int(line[1])


def preorder(tree: Node) -> None:
    """先行順巡回。"""
    print(f' {tree.key}', end='')
    if tree.left is not None:
        preorder(tree.left)
    if tree.right is not None:
        preorder(tree.right)


def inorder(tree: Node) -> None:
    """中間順巡回。"""
    if tree.left is not None:
        inorder(tree.left)
    print(f' {tree.key}', end='')
    if tree.right is not None:
        inorder(tree.right)


def get_node_inorder(node: Node) -> Node:
    """inorderで次の節点を返す。"""
    if node.left is not None:
        return get_node_inorder(node.left)
    return node
    if node.right is not None:
        return inorder(node.right)


def get_next_node(node: Node, order_type: str) -> Node:
    """次の節点を返す。"""
    if order_type == 'inorder':
        next_node = get_node_inorder(node.right)
    else:
        raise ValueError('未実装')
    return next_node


def insert(new_node: Node) -> None:
    """二分探索木に挿入する。"""

    # rootはglobalに共有する。
    global root

    # new_nodeを付け加える節(parent)の初期値をNoneに設定する。
    parent = None

    # tmpにrootを設定する。
    tmp = root

    # new_nodeを付け加える節(parent)を探索する。
    while tmp is not None:
        parent = tmp
        if new_node.key < tmp.key:
            tmp = tmp.left
        else:
            tmp = tmp.right

    # new_nodeの親を設定する。
    new_node.parent = parent

    # new_nodeの子供を設定する。
    if parent is None:
        # treeが空だった場合は、rootにnew_nodeを設定する。
        root = new_node
    elif new_node.key < parent.key:
        parent.left = new_node
    else:
        parent.right = new_node


def find(key)-> bool:
    if get_node(key) is None:
        return False
    else:
        return True


def get_node(key: int) -> Node:
    """キーが一致するノードを返す。"""
    global root

    node = root

    while node is not None:
        if key == node.key:
            return node
        elif key < node.key:
            node = node.left
        else:
            node = node.right

    return None


def count_child(node: Node) -> int:
    """ノードの子供の数を取得する。"""
    child_num = 0
    if node.left is not None:
        child_num += 1
    if node.right is not None:
        child_num += 1
    return child_num


def do_delete(node: Node) -> None:
    # delete対象がない場合はメソッドを終了する。
    if node is None:
        return

    child_num = count_child(node)
    parent = node.parent

    if parent is None:
        raise ValueError('親がないケース')

    # パターン1: nodeが子を持たない場合は、親から子へのリンクを削除する。
    if child_num == 0:
        if parent.left is not None and parent.left.key == node.key:
            parent.left = None
        else:
            parent.right = None

    # パターン2: nodeが子をひとつ持つ場合は、親から子へのリンクを親から孫へのリンクに変更する。
    elif child_num == 1:
        if parent.left is not None and parent.left.key == node.key:
            if node.left is not None:
                parent.left = node.left
                parent.left.parent = parent
            else:
                parent.left = node.right
                parent.left.parent = parent
        else:
            if node.left is not None:
                parent.right = node.left
                parent.right.parent = parent
            else:
                parent.right = node.right
                parent.right.parent = parent

    # パターン3: nodeが子をふたつ持つ場合は、inorderで次の節点を取得し、
    # 取得した節点のキーでnodeのキーを更新し、取得した節点を削除する。
    elif child_num == 2:
        next_node = get_next_node(node, 'inorder')
        node.key = next_node.key
        do_delete(next_node)
    else:
        raise ValueError('想定してない事態。child_numが0,1,2以外')


def delete(key: int) -> None:
    node = get_node(key)
    do_delete(node)


root = None  # treeの根を表す。初期値はNone。
N = int(input())
for _i in range(N):
    order, val = input_line()
    if order == 'insert':
        node = Node(val)
        insert(node)
    elif order == 'print':
        inorder(root)
        print()
        preorder(root)
        print()
    elif order == 'find':
        if find(val):
            print('yes')
        else:
            print('no')
    elif order == 'delete':
        delete(val)
