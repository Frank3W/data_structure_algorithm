"""
Module for linkedlist data structure and algorithms
"""

class LinkedNode():
    """Node for one-direction link.

    Parameters
    ----------
    data: any
        data stored in node

    Attributes
    ----------
    data: any
        data stored in node
    next: None or LinkedNode
        next node via the link
    """

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList():
    """Linked list of LinkedNode.

    Parameters
    ----------
    seq: iterable
        An iterable providing data

    """
    def __init__(self, seq):
        self.head = None

        curr = None
        for data in seq:
            if curr is None:
                curr = LinkedNode(data)
                self.head = curr
            else:
                next_node = LinkedNode(data)
                curr.next = next_node
                curr = next_node

    def to_list(self):
        """Converts to a list

        Returns
        -------
        list
            A list that contains data in linked list.

        """
        if self.head == None:
            return []
        else:
            converted = []

            curr = self.head
            while curr is not None:
                converted.append(curr.data)
                curr = curr.next

            return converted

    def reverse(self):
        """Revsers linkedlist in place.

        Returns
        -------
        None

        """
        if self.head is None:
            return

        curr = self.head
        curr_next = curr.next
        pre = None

        while curr_next is not None:
            curr.next = pre
            pre = curr
            curr = curr_next
            curr_next = curr.next

        curr.next = pre
        self.head = curr

