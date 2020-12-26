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
        seq_len = len(self)
        if seq_len == 0 or seq_len == 1:
            return

        for i in range(seq_len//2):
            tmp = self.data[i]
            self.data[i] = self.data[seq_len - 1 - i]
            self.data[seq_len - 1 - i] = tmp


class IntSequence(Sequence):

    def __init__(self, data):

        data = [int(_) for _ in data]
        super(IntSequence, self).__init__(data)
