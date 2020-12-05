from ..binarytree import BinaryTree

def test_dfs_recursive():
    fulllist = [1, 2, 3, 4, None]
    a_tree = BinaryTree.from_fulllist(fulllist)

    assert a_tree.dfs_recursive() == [1, 2, 4, 3]
