"""Module for implementation of binary tree.
"""

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

        level_cnt = 0 
        reach_end = False

        while True:
            level_cnt += 1
            start_idx = int(2 ** level_cnt) - 1
            curr_idx = start_idx
            next_level = []

            for curr_node in curr_level:
                if curr_idx >= size_list:
                    reach_end = True
                    break

                next_val = full_list[curr_idx]
                if next_val is None:
                    curr_node.left = None
                else:
                    next_node = BinaryNode(next_val)
                    curr_node.left = next_node
                    next_level.append(next_node)

                curr_idx += 1

                if curr_idx >= size_list:
                    reach_end = True
                    break

                next_val = full_list[curr_idx]
                if next_val is None:
                    curr_node.right = None
                else:
                    next_node = BinaryNode(next_val)
                    curr_node.right = next_node
                    next_level.append(next_node)

            if reach_end:
                break

            curr_level = next_level

        return cls(root)


    def dfs_recursive(self):
        """Depth First Search implemented in recursive manner.

        Returns
        -------
        list:
            list of data at nodes in depth first search order.
        """
        data_list = []
        BinaryTree._dfs_recursive(self.root, data_list)
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
            next_node = node_queue.pop()
            if next_node is not None:
                data_list.append(next_node.data)
                node_queue.push(next_node.left)
                node_queue.push(next_node.right)
            else:
                return data_list
    
    def tree_height(self):
        return BinaryTree._tree_height(self.root)

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
    def _dfs_recursive(node, array_list):
        """internal function for Depth First Search
        """

        if node is None:
            return

        array_list.append(node.data)

        if node.left is not None:
            BinaryTree._dfs_recursive(node.left, array_list)

        if node.right is not None:
            BinaryTree._dfs_recursive(node.right, array_list)

