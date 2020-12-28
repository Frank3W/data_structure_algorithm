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
