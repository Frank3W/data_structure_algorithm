from ..binarytree import BinaryTree

def test_dfs_recursive():
    fulllist = [1, 2, 3, 4, None]
    a_tree = BinaryTree.from_fulllist(fulllist)
    assert a_tree.dfs_recursive(order_type='preorder') == [1, 2, 4, 3]
    assert a_tree.dfs_recursive(order_type='inorder') == [4, 2, 1, 3]
    assert a_tree.dfs_recursive(order_type='postorder') == [4, 2, 3, 1]

def test_bfs_queue():
    fulllist = [1, 2, 3, 4, None]
    a_tree = BinaryTree.from_fulllist(fulllist)

    assert a_tree.bfs_queue() == [1, 2, 3, 4,]

def test_tree_height():
    empty_tree = BinaryTree.from_fulllist([])

    assert empty_tree.tree_height() == 0

    fulllist = [1, 2, 3, 4]
    a_tree = BinaryTree.from_fulllist(fulllist)

    assert a_tree.tree_height() == 3

def test_is_bst():
    a_tree = BinaryTree.from_fulllist([1, 2, 3, 4])
    assert not a_tree.is_bst()

    bst = BinaryTree.from_fulllist([2, 1, 3, -1])
    assert bst.is_bst()

def test_is_symmetric():
    a_tree = BinaryTree.from_fulllist([1, 2, 2, 3, 4, 4, 3])
    assert a_tree.is_symmetric()

    b_tree = BinaryTree.from_fulllist([1, 2, 3, 1, 3, None, 1])
    assert not b_tree.is_symmetric()

def test_level_traversal():
    a_tree = BinaryTree.from_fulllist([1, 2, 2, 3, None, 3, 3])
    a_list = a_tree.level_traversal()

    assert a_list[0] == [1]
    assert a_list[1] == [2, 2]
    assert a_list[2] == [3, None, 3, 3]

    a_tree = BinaryTree.from_fulllist([1, None, 3, 4, 5, 6, 7])
    a_list = a_tree.level_traversal()
    assert a_list[0] == [1]
    assert a_list[1] == [None, 3]
    assert a_list[2] == [4, 5]
    assert a_list[3] == [6, 7, None, None]

def test_left_view():
    a_tree = BinaryTree.from_fulllist([1, 2, 3, 4, 5])
    assert a_tree.left_view() == [1, 2, 4]

def test_top_bottom_view():
    a_tree = BinaryTree.from_fulllist([1, 2, 3, 4, 5, 6, 7])
    assert a_tree.top_bottom_view() == [4, 2, 1, 3, 7]
    assert a_tree.top_bottom_view(top=False) == [4, 2, 5, 3, 7]

def test_eq():
    a_tree = BinaryTree.from_fulllist([1, 2, 3, 4, 5])
    b_tree = BinaryTree.from_fulllist([1, 2, 3, 4, 5])
    c_tree = BinaryTree.from_fulllist([1, 2, None, 3, 5])
    d_tree = BinaryTree.from_fulllist([1, 2, None, 3, 5])
    empty_tree = BinaryTree(None)
    assert a_tree == b_tree
    assert not a_tree == c_tree
    assert not a_tree == empty_tree
    assert c_tree == d_tree

def test_dfs_stack():
    a_tree = BinaryTree.from_fulllist([1, 2, 3, 4, 5])
    assert a_tree.dfs_stack() == a_tree.dfs_recursive()
    assert a_tree.dfs_stack(order_type='preorder') == a_tree.dfs_stack(order_type='preorder')
    assert a_tree.dfs_stack(order_type='postorder') == a_tree.dfs_recursive(order_type='postorder')
