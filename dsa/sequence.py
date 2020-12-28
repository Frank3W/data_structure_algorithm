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

    def negative_all_front(self):
        """Moves all negatives to the front in place.
        """
        if len(self.data) <= 1:
            return

        front_idx = 0
        end_idx = len(self.data) - 1

        while front_idx < end_idx:
            if self.data[front_idx] < 0:
                front_idx += 1
                continue

            if self.data[end_idx] >= 0:
                end_idx -= 1
                continue

            tmp = self.data[front_idx]
            self.data[front_idx] = self.data[end_idx]
            self.data[end_idx] = tmp

            front_idx += 1
            end_idx -= 1


    def longest_consecutive_subseq(self):
        """Gets longest subsequence such that it covers consecutive numbers.
        """
        data_copy = [_ for _ in self.data]
        if len(self.data) <= 1:
            return data_copy

        data_sorted = list(enumerate(self.data))
        data_sorted = sorted(data_sorted, key=lambda x: x[1])

        # remove duplicats
        real_idx = None

        for front_idx, item in enumerate(data_sorted):
            value = item [1]

            if real_idx is None:
                real_idx = 0
            else:
                if value != data_sorted[real_idx][1]:
                    real_idx += 1
                    data_sorted[real_idx] = data_sorted[front_idx]

        data_sorted_np_dulicats = data_sorted[:real_idx+1]

        longest_len = 1
        longest_begin = 0
        longest_end = 0

        start_idx = 0

        while True:
            stopped = False

            if start_idx == len(data_sorted_np_dulicats) - 1:
                curr_idx = start_idx + 1
            else:
                for curr_idx in range(start_idx+1, len(data_sorted_np_dulicats)):
                    curr_val = data_sorted_np_dulicats[curr_idx][1]
                    pre_val = data_sorted_np_dulicats[curr_idx-1][1]
                    if curr_val > pre_val + 1:
                        stopped = True
                        break

                if not stopped:
                    curr_idx = curr_idx + 1

            curr_len = curr_idx - start_idx
            if curr_len > longest_len:
                longest_len = curr_len
                longest_begin = start_idx
                longest_end = curr_idx - 1

            if stopped:
                start_idx = curr_idx
            else:
                break

        idx_list = [_[0] for _ in data_sorted_np_dulicats[longest_begin:(longest_end+1)]]
        idx_list.sort()

        return longest_len, [self.data[_] for _ in idx_list]










