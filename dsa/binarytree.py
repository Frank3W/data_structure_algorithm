"""Module for implementation of binary tree.
"""

import os

from .linkedlist import LinkedQueue

class BinaryNode:
    """Binary tree node.
    """

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    """Binary tree implementation.
    """

    def __init__(self, root):
        self.root = root

    @classmethod
    def from_fulllist(cls, full_list):
        """Generates tree object from a full binary list.

        None in the full_list indicates no-node.

        Returns
        -------
        BinaryTree

        """
        if len(full_list) == 0:
            return cls(None)


        size_list = len(full_list)

        curr_level = []

        root = BinaryNode(full_list[0])
        curr_level.append(root)

        next_idx = 1
        reach_end = False

        while True:
            next_level = []
            for curr_node in curr_level:
                if next_idx >= size_list:
                    reach_end = True
                    break

                next_val = full_list[next_idx]
                if next_val is None:
                    curr_node.left = None
                else:
                    next_node = BinaryNode(next_val)
                    curr_node.left = next_node
                    next_level.append(next_node)

                next_idx += 1

                if next_idx >= size_list:
                    reach_end = True
                    break

                next_val = full_list[next_idx]
                if next_val is None:
                    curr_node.right = None
                else:
                    next_node = BinaryNode(next_val)
                    curr_node.right = next_node
                    next_level.append(next_node)

                next_idx += 1

            if reach_end:
                break

            if len(next_level) == 0:
                break

            curr_level = next_level

        return cls(root)


    def dfs_recursive(self, order_type='inorder'):
        """Depth First Search implemented in recursive manner.

        Returns
        -------
        list:
            list of data at nodes in depth first search order.
        """
        data_list = []
        BinaryTree._dfs_recursive(self.root, data_list, order_type=order_type)
        return data_list

    def bfs_queue(self):
        """Breadth First Search implemneted by Queue.

        Returns
        -------
        list:
            list of data at nodes in breadth first search order.
        """

        if self.root is None:
            return

        node_queue = LinkedQueue()
        node_queue.push(self.root)

        data_list = []

        while True:
            if node_queue.is_empty():
                return data_list
            next_node = node_queue.pop()
            if next_node is not None:
                data_list.append(next_node.data)
                node_queue.push(next_node.left)
                node_queue.push(next_node.right)

    def to_str(self, base_len=1):
        """Converts to a printable string.

        Parameters
        ----------
            base_len:int
                number of whitespace as a separation base for between nodes

        Returns
        -------
        str
        """

        base_len = int(base_len)
        if base_len <= 0:
            raise ValueError('base_len should be a positive integer.')

        if self.root is None:
            return
        h = self.tree_height()
        root_wspace = base_len * (2 ** h - 1)
        curr_level = LinkedQueue()
        curr_level.push([self.root, root_wspace])

        level_lists = []
        is_all_none = False
        offset = base_len * (2 ** (h - 1))

        while not is_all_none:
            is_all_none = True
            next_level = LinkedQueue()
            curr_list = []
            for items in curr_level:
                curr_node = items[0]
                curr_wspace = items[1]

                if curr_node is None:
                    continue
                else:
                    curr_list.append([curr_node.data, curr_wspace])

                if curr_node.left is not None or curr_node.right is not None:
                    is_all_none = False
                next_level.push([curr_node.left, curr_wspace - offset])
                next_level.push([curr_node.right, curr_wspace + offset])

            level_lists.append(curr_list)
            offset /= 2
            curr_level = next_level

        tree_str = ''
        for line_list in level_lists:
            level_str = ''
            for items in line_list:
                curr_wspace = int(items[1])
                if curr_wspace < len(level_str):
                    level_str = level_str[:curr_wspace]
                else:
                    level_str += (' ' * (curr_wspace - len(level_str)))

                level_str += str(items[0])
            tree_str += level_str
            tree_str += os.linesep
        return tree_str


    def level_traversal(self, stop_at_none=True):
        """Level-order tree traversal

        Parameters
        ----------
            stop_at_none:bool
                If True, traveral stops at None. Otherwise, traveral continues assumeing
                None has two child nodes of None until reaching at the tree bottom.

        Returns
        -------
        list:
            list of list of data at tree node.
        """

        if self.root is None:
            return

        levels_list = []

        curr_level = LinkedQueue()
        curr_level.push(self.root)
        is_all_none = False

        while not is_all_none:
            is_all_none = True
            next_level = LinkedQueue()
            curr_level_list = []
            while True:
                if curr_level.is_empty():
                    curr_level = next_level
                    levels_list.append(curr_level_list)
                    break

                curr_node = curr_level.pop()

                if curr_node is None:
                    curr_level_list.append(None)
                    if stop_at_none:
                        continue
                else:
                    curr_level_list.append(curr_node.data)

                if curr_node is not None:
                    if curr_node.left is not None or curr_node.right is not None:
                        is_all_none = False
                    next_level.push(curr_node.left)
                    next_level.push(curr_node.right)
                else:
                    # only occurs when stop_at_none is False
                    next_level.push(None)
                    next_level.push(None)

        return levels_list

    def left_view(self):
        """Gets tree view from left side.

        Returns
        -------
        list
        """

        if self.root is None:
            return None

        curr_level = LinkedQueue()
        curr_level.push(self.root)

        is_all_none = False
        left_view_list = []

        while not is_all_none:
            is_all_none = True

            first_non_none = True
            next_level = LinkedQueue()
            for curr_node in curr_level:
                if curr_node is None:
                    continue
                else:
                    if first_non_none:
                        first_non_none = False
                        left_view_list.append(curr_node.data)

                    if curr_node.left is not None or curr_node.right is not None:
                        is_all_none = False
                    next_level.push(curr_node.left)
                    next_level.push(curr_node.right)

            curr_level = next_level

        return left_view_list


    def tree_height(self):
        """Gets tree height.
        """
        return BinaryTree._tree_height(self.root)

    def is_bst(self):
        """Whether is a binary search tree

        Returns
        -------
        bool:
            True if it is a binary search tree and False otherwise
        """

        if self.root is None:
            return True

        data_list = []
        is_bst = BinaryTree._dfs_bst(self.root, data_list)

        return is_bst

    def is_symmetric(self):
        """Whether is symmetric.

        Returns
        -------
        bool:
            True if it is a symmetric binary tree.
        """
        if self.root is None:
            return True

        return BinaryTree._is_symmetric(self.root.left, self.root.right)

    @staticmethod
    def _is_symmetric(leftnode, rightnode):
        if leftnode is None and rightnode is None:
            return True
        elif leftnode is None and rightnode is not None:
            return False
        elif leftnode is not None and rightnode is None:
            return False
        else:
            left_symmetric = BinaryTree._is_symmetric(leftnode.left, rightnode.right)
            right_symmetric = BinaryTree._is_symmetric(leftnode.right, rightnode.left)
            return left_symmetric and right_symmetric

    @staticmethod
    def _dfs_bst(node, data_list):
        """internal function for Depth First Serach to verify BFS.
        """

        if node is None:
            return True

        left_tree = BinaryTree._dfs_bst(node.left, data_list)

        if not left_tree:
            return left_tree

        next_val = node.data
        if len(data_list) != 0 and next_val < data_list[-1]:
            return False

        data_list.append(next_val)

        right_tree = BinaryTree._dfs_bst(node.right, data_list)

        return right_tree


    @staticmethod
    def _tree_height(node):
        """internal function for computing tree height.
        """

        if node is None:
            return 0
        else:
            left_height = 1 + BinaryTree._tree_height(node.left)
            right_height = 1 + BinaryTree._tree_height(node.right)
            return max(left_height, right_height)


    @staticmethod
    def _dfs_recursive(node, array_list, order_type):
        """internal function for Depth First Search in preoder.
        """

        if order_type not in ['inorder', 'preorder', 'postorder']:
            raise ValueError('order_type must be one of ["inorder", "preorder", "postorder"]')


        if node is None:
            return

        if order_type == 'preorder':
            array_list.append(node.data)

        if node.left is not None:
            BinaryTree._dfs_recursive(node.left, array_list, order_type)

        if order_type == 'inorder':
            array_list.append(node.data)

        if node.right is not None:
            BinaryTree._dfs_recursive(node.right, array_list, order_type)

        if order_type == 'postorder':
            array_list.append(node.data)

