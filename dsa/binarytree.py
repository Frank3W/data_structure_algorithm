"""Module for implementation of binary tree.
"""

import os

from .linkedlist import LinkedQueue
from .linkedlist import DoubleLinkedNode

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

    def __init__(self, root=None):
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

    def least_common_ancestor(self, val1, val2):
        if self.root is None:
            return None

        node_stack = []
        first_val = None
        second_val = None

        first_val_found = False
        second_val_found = False

        curr_node = self.root
        while curr_node is not None:
            node_stack.append([curr_node, False, False])
            if not first_val_found:
                if curr_node.data in [val1, val2]:
                    first_val = curr_node.data
                    first_val_found = True
                    if first_val == val1:
                        second_val = val2
                    else:
                        second_val = val1

                    for item in node_stack:
                        item[2] = True
            else:
                if curr_node.data == second_val:
                    second_val_found = True

            curr_node = curr_node.left

        while len(node_stack) != 0:
            if not node_stack[-1][1]:
                node_stack[-1][1] = True
                visit_node = node_stack[-1][0]

                curr_node = visit_node.right
                while curr_node is not None:
                    node_stack.append([curr_node, False, False])
                    if not first_val_found:
                        if curr_node.data in [val1, val2]:
                            first_val = curr_node.data
                            first_val_found = True
                            if first_val == val1:
                                second_val = val2
                            else:
                                second_val = val1

                            for item in node_stack:
                                item[2] = True
                    else:
                        if curr_node.data == second_val:
                            second_val_found = True

                    curr_node = curr_node.left
            else:
                pop_item = node_stack.pop()
                if first_val_found and second_val_found and pop_item[2]:
                    return pop_item[0].data

        return None



    def dfs_stack(self, order_type='inorder'):
        if order_type == 'preorder' or order_type == 'inorder':
            return self._dfs_stack_pre_in_order(order_type)
        elif order_type == 'postorder':
            return self._dfs_stack_postorder()
        else:
            raise ValueError('order_type is not supported')

    def _dfs_stack_postorder(self):
        if self.root is None:
            return None

        val_list = []
        node_stack = []

        curr_node = self.root
        while curr_node is not None:
            node_stack.append([curr_node, False])
            curr_node = curr_node.left

        while len(node_stack) != 0:
            if not node_stack[-1][1]:
                node_stack[-1][1] = True
                visit_node = node_stack[-1][0]

                curr_node = visit_node.right
                while curr_node is not None:
                    node_stack.append([curr_node, False])
                    curr_node = curr_node.left
            else:
                pop_pair = node_stack.pop()
                val_list.append(pop_pair[0].data)

        return val_list

    def _dfs_stack_pre_in_order(self, order_type='inorder'):
        if self.root is None:
            return None

        val_list = []
        node_stack = []

        curr_node = self.root
        while curr_node is not None:
            node_stack.append(curr_node)
            if order_type == 'preorder':
                val_list.append(curr_node.data)
            curr_node = curr_node.left


        while len(node_stack) != 0:
            visit_node = node_stack.pop()
            if order_type == 'inorder':
                val_list.append(visit_node.data)

            if visit_node.right is not None:
                node_stack.append(visit_node.right)
                if order_type == 'preorder':
                    val_list.append(visit_node.right.data)
                curr_node = visit_node.right.left
                while curr_node is not None:
                    node_stack.append(curr_node)
                    if order_type == 'preorder':
                        val_list.append(curr_node.data)
                    curr_node = curr_node.left

        return val_list


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

    def to_dll(self):
        """Converts to double linked list
        """
        if self.root is None:
            return None

        begin_node, end_node = BinaryTree._to_dll_recursive(self.root)
        return begin_node, end_node

    @staticmethod
    def _to_dll_recursive(node):
        # node must be not none
        begin_node = None
        end_node = None

        curr_dll_node = DoubleLinkedNode(node.data)

        if node.left is None and node.right is None:
            begin_node = curr_dll_node
            end_node = curr_dll_node

        elif node.left is None and node.right is not None:
            right_begin, right_end = BinaryTree._to_dll_recursive(node.right)
            begin_node = curr_dll_node
            end_node = right_end

            # connect nodes
            curr_dll_node.next = right_begin
            right_begin.pre = curr_dll_node
        elif node.left is not None and node.right is None:
            left_begin, left_end = BinaryTree._to_dll_recursive(node.left)
            begin_node = left_begin
            end_node = curr_dll_node

            # connect nodes
            left_end.next = curr_dll_node
            curr_dll_node.pre = left_end
        else:
            left_begin, left_end = BinaryTree._to_dll_recursive(node.left)
            right_begin, right_end = BinaryTree._to_dll_recursive(node.right)
            begin_node = left_begin
            end_node = right_end

            # connect nodes
            left_end.next = curr_dll_node
            curr_dll_node.pre = left_end

            curr_dll_node.next = right_begin
            right_begin.pre = curr_dll_node

        begin_node.pre = None
        end_node.next = None

        return begin_node, end_node


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

    def top_bottom_view(self, top=True):
        node_dist_lists = self._distance_by_level()

        if node_dist_lists is None or len(node_dist_lists) == 0:
            return None

        view_dict = {}

        if top:
            loop_list = node_dist_lists
        else:
            loop_list = node_dist_lists[::-1]

        for level_list in loop_list:
            for item in level_list:
                curr_val = item[0]
                curr_dist = item[1]
                if curr_dist not in view_dict:
                    view_dict[curr_dist] = curr_val

        sorted_pairs = sorted(view_dict.items(), key=lambda x: x[0])
        sorted_values = [item[1] for item in sorted_pairs]

        return sorted_values


    def _distance_by_level(self, delta_unit=1):

        if self.root is None:
            return None

        curr_level = []
        curr_level.append([self.root, 0])

        dist_lists = []

        while True:
            next_level = []
            curr_list = []

            for curr_item in curr_level:
                curr_node = curr_item[0]
                curr_dist = curr_item[1]

                curr_list.append([curr_node.data, curr_dist])

                if curr_node.left is not None:
                    next_level.append([curr_node.left, curr_dist - delta_unit])

                if curr_node.right is not None:
                    next_level.append([curr_node.right, curr_dist + delta_unit])

            dist_lists.append(curr_list)

            if len(next_level) != 0:
                curr_level = next_level
            else:
                break

        return dist_lists


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

    def find_largest_bst(self):
        """Finds a binary search subtree of largest size

        Returns
        -------
        tuple:
            value at root of the binary search subtree of largest size.
            size of the binary search subtree
            minimum value of the binary search subtree
            maximum value of the binary search subtree
        """

        node_val, bts_size, bts_min, bts_max, tree_size = self._find_largest_bst_recursive(self.root)
        return node_val, bts_size, bts_min, bts_max

    def _find_largest_bst_recursive(self, node):
        if node.right is None and node.left is None:
            return node.data, 1, node.data, node.data, 1

        if node.left is not None:
            left_root_data, left_bts_size, left_bts_min, left_bts_max, left_size = self._find_largest_bst_recursive(node.left)

        if node.right is not None:
            right_root_data, right_bts_size, right_bts_min, right_bts_max, right_size = self._find_largest_bst_recursive(node.right)

        if node.left is not None and node.right is None:
            if left_bts_size == left_size and left_bts_max < node.data:
                return node.data, left_bts_size + 1, left_bts_min, node.data, left_size + 1
            else:
                return node.data, left_bts_size, left_bts_min, left_bts_max, left_size + 1
        elif node.right is None and node.right is not None:
            if right_bts_size == right_size and right_bts_min > node.data:
                return node.data, right_bts_size + 1, node.data, right_bts_max, right_size + 1
            else:
                return right_root_data, right_bts_size, right_bts_min, right_bts_max, right_size + 1
        else:
            if left_bts_size == left_size and left_bts_max < node.data and right_bts_size == right_size and right_bts_min > node.data:
                return node.data, left_bts_size + right_bts_size + 1, left_bts_min, right_bts_max, left_size + right_size + 1
            else:
                if left_bts_size >= right_bts_size:
                    return left_root_data, left_bts_size, left_bts_min, left_bts_max, left_size + right_size + 1
                else:
                    return right_root_data, right_bts_size, right_bts_min, right_bts_max, left_size + right_size + 1


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

    def __eq__(self, other):
        if self.root is None and other.root is None:
            return True
        elif self.root is not None and other.root is not None:
            self_levels = self.level_traversal()
            other_levels = other.level_traversal()
            if len(self_levels) != len(other_levels):
                return False
            else:
                for i in range(len(self_levels)):
                    if self_levels[i] != other_levels[i]:
                        return False
                return True
        else:
            return False

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

