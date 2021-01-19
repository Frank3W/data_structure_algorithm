from ..sequence import IntSequence
from ..sequence import Sequence

def test_reverse():
    a_seq = Sequence(['a', 'b', 'c'])
    a_seq.reverse()

    assert list(a_seq) == ['c', 'b', 'a']

    b_seq = Sequence([])
    a_seq.reverse()

    assert len(list(b_seq)) == 0

    int_seq = IntSequence([1, '2', 3])
    int_seq.reverse()

    assert list(int_seq) == [3, 2, 1]

def test_rm_duplicates():
    a_seq = Sequence(['c', 'a', 'a', 'b', 'c', 'd', 'o'])
    a_seq.rm_duplicates()
    assert list(a_seq) == ['c', 'a', 'b', 'd', 'o']

def test_rotate2right():
    a_seq = Sequence(['a', 'b', 'c'])
    a_seq.rotate2right(1)
    assert list(a_seq) == ['c', 'a', 'b']
    a_seq.rotate2right(2)
    assert list(a_seq) == ['a', 'b', 'c']

def test_longest_consecutive_subseq():
    a_seq = IntSequence([11, 3, 1, 2, 12, 14, 13, 15, 0])
    max_len, sub_seq = a_seq.longest_consecutive_subseq()
    assert max_len == 5
    assert sub_seq == [11, 12, 14, 13, 15]

def test_negative_all_front():
    a_seq = IntSequence([-1, 6, -2, 13, -9, 11, 21])
    a_seq.negative_all_front()
    assert set(a_seq[:3]) == set([-1, -2, -9])

def test_maxsum_contiguous():
    a_seq = IntSequence([-2, -10, -1])
    assert list(a_seq.maxsum_contiguous()) == [-1, 2, 2]

    b_seq = IntSequence([-1, 2, 3, 5, -2])
    assert list(b_seq.maxsum_contiguous()) == [10, 1, 3]

def is_wave(seq):
    seq_list = list(seq)

    if len(seq_list) <= 2:
        return True

    # expectation for next item
    go_up = None
    for idx in range(len(seq_list)):
        if idx >= 1:
            if seq_list[idx] > seq_list[idx-1]:
                if go_up is None:
                    go_up = False
                else:
                    if not go_up:
                        return False
                    else:
                        go_up = False
            elif seq_list[idx] < seq_list[idx-1]:
                if go_up is None:
                    go_up = True
                else:
                    if go_up:
                        return False
                    else:
                        go_up = True
            else:
                if go_up is not None:
                    go_up = not go_up

    return True


def test_wave_sequence():
    a_seq = IntSequence([1, -2, 1, 3, 1, 2, 0, -1, 3, 5, -9])
    a_seq.wave_sequence()

    assert is_wave(a_seq)

def test_alternative_negative_positive():
    a_seq = IntSequence(range(-3, 5))
    a_seq.alternative_negative_positive()
    assert list(a_seq) == [-3, 0, -2, 1, -1, 2, 3, 4]

    b_seq = IntSequence([1, 2, 3, 4])
    b_seq.alternative_negative_positive()
    assert list(b_seq) == [1, 2, 3, 4]

def test_zerosum_subarray():
    a_seq = IntSequence([1, -3, 3])
    has_zerosum, idx_pair = a_seq.zerosum_subarray()
    assert has_zerosum
    assert idx_pair[0] == 1
    assert idx_pair[1] == 2

def test_find_largest():
    a_seq = IntSequence(range(10))
    for i in range(10):
        assert a_seq.find_largest(i+1) == 9 - i

def test_find_frequent():
    a_seq = IntSequence([1, 1, 1, 1, 2, 2, 2, 3, 3, 5])
    assert set(a_seq.find_frequent(3)) == set([1])
    assert set(a_seq.find_frequent(4)) == set([2, 1])

def test_gen_idx_first_smaller():
    a_seq = IntSequence([1, 2, 3])
    assert a_seq.gen_idx_first_smaller() == [-1, 0, 1]

    b_seq = IntSequence([1, 2, 4, -1, 10])
    assert b_seq.gen_idx_first_smaller() == [-1, 0, 1, -1, 3]
