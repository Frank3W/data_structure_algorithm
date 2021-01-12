""" Module for a simple implementation of heap
"""

class Heap:
    """Min heap functional class
    """

    @staticmethod
    def heapify(data):
        """Heapify the data list in place in minimal manner.

        Parameters
        ----------
            data: list

        Returns
        -------
            None
        """

        size = len(data)
        if size <= 1:
            return

        for idx in range(Heap._parent(size-1), -1, -1):
            curr_idx = idx
            while True:
                next_idx = Heap._heapify_one_node(data, curr_idx, size)
                if next_idx == curr_idx:
                    break
                else:
                    curr_idx = next_idx

    @staticmethod
    def rm_root(data):
        """Remove the first element of the heapified list.

        Parameters
        ----------
            data: list

        Returns
        -------
            list
                reduced list
        """

        size = len(data)
        if size <= 0:
            raise ValueError('Size must be positive.')

        if size == 1:
            return data[0:0]

        tmp = data[0]
        data[0] = data[size-1]
        data[size-1] = tmp

        size = size - 1

        curr_idx = 0
        while True:
            next_idx = Heap._heapify_one_node(data, curr_idx, size)
            if next_idx == curr_idx:
                break
            else:
                curr_idx = next_idx

        return data[:size]

    @staticmethod
    def replace_root(data, element):
        """Replace the first element of the heapified list by the input element.

        Parameters
        ----------
            data: list
            element: any

        Returns
        -------
            None
        """

        size = len(data)
        if size <= 0:
            raise ValueError('Size must be positive.')

        data[0] = element
        if size == 1:
            return

        curr_idx = 0

        while True:
            next_idx = Heap._heapify_one_node(data, curr_idx, size)
            if next_idx == curr_idx:
                break
            else:
                curr_idx = next_idx

    @staticmethod
    def add(data, element):
        """Add an element to the heapified list.

        Parameters
        ----------
            data: list
            element: any

        Returns
        -------
            None
        """

        data.append(element)
        size = len(data)

        if size == 1:
            return data

        curr_idx = size - 1
        next_idx = Heap._parent(curr_idx)
        while True:
            if next_idx == -1:
                return data
            if data[next_idx] <= data[curr_idx]:
                return data
            tmp = data[next_idx]
            data[next_idx] = data[curr_idx]
            data[curr_idx] = tmp
            curr_idx = next_idx
            next_idx = Heap._parent(curr_idx)

        return data


    @staticmethod
    def _heapify_one_node(data, idx, size):
        """internal function - heapify at one node.

        Returns
        -------
            int
                index to which idx is moved. If no action happens, idx is returned.
        """
        left_idx = Heap._leftchild(idx, size)
        right_idx = Heap._rightchild(idx, size)


        if right_idx == -1 and left_idx == -1:
            return idx
        elif right_idx == -1 and left_idx != -1:
            if data[idx] > data[left_idx]:
                tmp = data[idx]
                data[idx] = data[left_idx]
                data[left_idx] = tmp
                return left_idx
            return idx
        else:
            min_val = min(data[idx], data[left_idx], data[right_idx])
            if min_val != data[idx]:
                if min_val == data[left_idx]:
                    tmp = data[left_idx]
                    data[left_idx] = data[idx]
                    data[idx] = tmp
                    return left_idx
                else:
                    tmp = data[right_idx]
                    data[right_idx] = data[idx]
                    data[idx] = tmp
                    return right_idx
            return idx


    @staticmethod
    def _leftchild(idx, size):
        l_idx = 2 * idx + 1
        if l_idx >= size:
            return -1
        else:
            return l_idx

    @staticmethod
    def _rightchild(idx, size):
        r_idx = 2 * idx + 2
        if r_idx >= size:
            return -1
        else:
            return r_idx

    @staticmethod
    def _parent(idx):
        if idx == 0:
            return -1
        else:
            return (idx - 1)//2
