"""
Module for linkedlist data structure and algorithms
"""

class LinkedNode:
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


class LinkedList:
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

    def even_odd_switch(self):
        """Reorder even and odd nodes in place.

        Odd nodes will be followed by even nodes in the resulting linkedlist.

        """

        if self.head is None or self.head.next is None:
            return

        odd_head = self.head
        even_head = self.head.next

        odd_tail = odd_head
        even_tail = even_head

        odd_curr = odd_head.next.next

        while True:
            # odd_curr always point to next element in original linked list
            if odd_curr is None:
                odd_tail.next = even_head
                even_tail.next = None
                break
            elif odd_curr.next is None:
                odd_tail.next = odd_curr
                odd_curr.next = even_head
                even_tail.next = None
                break
            else:
                odd_tail.next = odd_curr
                even_tail.next = odd_curr.next

                odd_tail = odd_tail.next
                even_tail = even_tail.next

                odd_curr = odd_curr.next.next

    def delete(self, data):
        """Delete first occurrence of node with input data.

        Returns
        -------
        bool
            indicator whether element is deleted or not.

        """

        if self.head is None:
            return False

        if self.head.data == data:
            self.head = self.head.next
            return True

        pre = self.head
        curr = self.head.next

        while curr is not None:
            if curr.data == data:
                pre.next = curr.next
                return True
            else:
                pre = curr
                curr = curr.next

        return False

    def middle(self):
        """Gets the middle element.

        Returns None if linkedlist is empty.
        """

        if self.head is None:
            return None

        curr = self.head
        curr_t2 = self.head.next

        while curr_t2 is not None and curr_t2.next is not None:
            curr = curr.next
            curr_t2 = curr_t2.next.next

        return curr.data


class LinkedStack(LinkedList):
    """Linked list implementation of Stack
    """

    def __init__(self):
        super(LinkedStack, self).__init__([])

    def pop(self):
        """Removes first element.

        Returns
        -------
        any

        """
        if self.head is None:
            return None

        curr = self.head
        self.head = self.head.next
        return curr.data

    def push(self, data):
        """Adds an element to the stack

        Args
        ----
        data: any

        """
        
        node = LinkedNode(data)

        if self.head is None:
            self.head = node
        else:
            head_next = self.head
            self.head = node
            node.next = head_next

