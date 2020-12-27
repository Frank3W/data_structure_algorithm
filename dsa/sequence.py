"""Module for sequence data structure"""


class Sequence:

    def __init__(self, data):
        self.data = [ _ for _ in data]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, i):
        return self.data[i]

    def __iter__(self):
        for i in range(len(self.data)):
            yield self.data[i]

    def reverse(self):
        """Reverse data in place"""

        seq_len = len(self)
        if seq_len == 0 or seq_len == 1:
            return

        for i in range(seq_len//2):
            tmp = self.data[i]
            self.data[i] = self.data[seq_len - 1 - i]
            self.data[seq_len - 1 - i] = tmp

    def rm_duplicates(self):
        """Removes duplicates in place"""

        if len(self.data) == 0 or len(self.data) == 1:
            return None

        visited_set = set()

        r_idx = 0
        for i in range(len(self.data)):
            if self.data[i] in visited_set:
                continue
            else:
                visited_set.add(self.data[i])
                self.data[r_idx] = self.data[i]
                r_idx += 1

        self.data = self.data[:r_idx]

    def rotate2right(self, k):
        """Rotates k positions to the right.

        Parameters
        ----------
            k: int
                number of position to rotate to right
        """

        if k != int(k) or k < 0:
            raise ValueError('k must be a positive integer.')

        len_data = len(self.data)

        if len_data == 0 or len_data == 1:
            return

        k = k % len_data

        if k == 0:
            return

        # rotate by k
        tmp = self.data[(len_data - k):]
        self.data[k:] = self.data[:(len_data-k)]
        self.data[:k] = tmp


class IntSequence(Sequence):

    def __init__(self, data):

        data = [int(_) for _ in data]
        super(IntSequence, self).__init__(data)
