"""Module for sequence data structure"""

from .linkedlist import LinkedQueue
from .heap import Heap


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


    def find_largest(self, k):
        if k <= 0 or k != int(k):
            raise ValueError('k must be a positive integer.')

        k_heap = [ _ for _ in self.data[:k]]
        Heap.heapify(k_heap)

        for idx in range(k, len(self.data)):
            curr_val = self.data[idx]
            if curr_val > k_heap[0]:
                Heap.replace_root(k_heap, curr_val)

        return k_heap[0]

    def find_frequent(self, k):
        """Find elements with frequency > n/k where n is sequence length
        """

        if k <= 1 or k != int(k):
            raise ValueError('k must be a positive integer >= 2.')

        stack_list = []
        for i in range(k-1):
            stack_list.append([])

        for curr_val in self.data:
            is_existent = False

            empty_stack = None
            for curr_stack in stack_list:
                if len(curr_stack) == 0:
                    empty_stack = curr_stack
                else:
                    if curr_val == curr_stack[-1]:
                        curr_stack.append(curr_val)
                        is_existent = True
            if not is_existent:
                if empty_stack is not None:
                    empty_stack.append(curr_val)
                else:
                    for curr_stack in stack_list:
                        curr_stack.pop()

        val_dict = {}
        for curr_stack in stack_list:
            if len(curr_stack) != 0:
                val_dict[curr_stack[0]] = 0

        for curr_val in self.data:
            if curr_val in val_dict:
                val_dict[curr_val] += 1

        freq_list = []

        threshold = len(self.data) // k

        for key, value in val_dict.items():
            if value > threshold:
                freq_list.append(key)

        return freq_list


    def maxsum_contiguous(self):
        """Gets contiguous subarray with max sum.
        """
        if len(self.data) == 0:
            return None

        if len(self.data) == 1:
            return self.data[0]

        # kth is the max sum of contiguous subarray in self.data[:(k+1)]
        mem_maxsum = []
        # kth is the max sum of contiguous subarray ending at kth position in self.data[:(k+1)]
        mem_maxsum_last_included = []

        start_idx = 0
        end_idx = 0

        start_idx_last_included = 0

        mem_maxsum.append(self.data[0])
        mem_maxsum_last_included.append(self.data[0])

        # dynamic programming in linear fashion
        for idx in range(1, len(self.data)):
            curr_val = self.data[idx]
            maxsum_last_included = max(curr_val + mem_maxsum_last_included[-1], curr_val)
            if maxsum_last_included == curr_val:
                start_idx_last_included = idx

            maxsum = max(maxsum_last_included, mem_maxsum[-1])

            if maxsum == maxsum_last_included:
                start_idx = start_idx_last_included
                end_idx = idx

            mem_maxsum_last_included.append(maxsum_last_included)
            mem_maxsum.append(maxsum)

        return mem_maxsum[-1], start_idx, end_idx


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

    def wave_sequence(self):
        """Converts the sequence into waving pattern, i.e., a_1 <= a_2 >= a_3 <= a_4 >= a_5 ...
        """

        if len(self.data) <= 2:
            return

        if self.data[0] < self.data[1]:
            go_up = False
        else:
            go_up = True

        for idx in range(2, len(self.data)):
            if go_up:
                if self.data[idx] < self.data[idx-1]:
                    tmp = self.data[idx]
                    self.data[idx] = self.data[idx-1]
                    self.data[idx-1] = tmp
                go_up = False
            else:
                if self.data[idx] > self.data[idx-1]:
                    tmp = self.data[idx]
                    self.data[idx] = self.data[idx-1]
                    self.data[idx-1] = tmp
                go_up = True


    def alternative_negative_positive(self):

        if len(self.data) <= 1:
            return

        expected_neg = True
        idx_considered_next = 0

        neg_queue = LinkedQueue()
        pos_queue = LinkedQueue()

        for idx in range(len(self.data)):
            if self.data[idx] < 0:
                if expected_neg:
                    self.data[idx_considered_next] = self.data[idx]
                    idx_considered_next += 1
                    if not pos_queue.is_empty():
                        next_val = pos_queue.pop()
                        self.data[idx_considered_next] = next_val
                        idx_considered_next += 1
                    else:
                        expected_neg = False
                else:
                    neg_queue.push(self.data[idx])
            else:
                if expected_neg:
                    pos_queue.push(self.data[idx])
                else:
                    self.data[idx_considered_next] = self.data[idx]
                    idx_considered_next += 1
                    if not neg_queue.is_empty():
                        next_val = neg_queue.pop()
                        self.data[idx_considered_next] = next_val
                        idx_considered_next += 1
                    else:
                        expected_neg = True

        if idx_considered_next < len(self.data):
            while not pos_queue.is_empty():
                next_val = pos_queue.pop()
                self.data[idx_considered_next] = next_val
                idx_considered_next += 1

            while not neg_queue.is_empty():
                next_val = neg_queue.pop()
                self.data[idx_considered_next] = next_val
                idx_considered_next += 1

    def zerosum_subarray(self):
        """Finds a subarray with sum equal 0.
        """

        if len(self.data) == 0:
            return None

        cumsum_dict = {}
        curr_sum = 0

        for idx, item in enumerate(self.data):
            curr_sum += item

            if curr_sum == 0:
                return True, [0, idx]

            if curr_sum in cumsum_dict:
                return True, [cumsum_dict[curr_sum]+1, idx]

            cumsum_dict[curr_sum] = idx

        return False, None


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
