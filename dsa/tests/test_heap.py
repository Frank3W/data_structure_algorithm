from ..heap import Heap

def test_heapify():
    a_list = [3, 1, 5, 2, 9]
    Heap.heapify(a_list)
    assert a_list[0] == 1

    a_list = [3]
    Heap.heapify(a_list)
    assert a_list[0] == 3

    a_list = [3, 1]
    Heap.heapify(a_list)
    assert a_list[0] == 1

def test_rm_root():
    a_list = [3, 1, 5, 2, 9]
    Heap.heapify(a_list)

    assert a_list[0] == 1

    a_list = Heap.rm_root(a_list)
    assert a_list[0] == 2

    a_list = Heap.rm_root(a_list)
    assert a_list[0] == 3

    a_list = Heap.rm_root(a_list)
    assert a_list[0] == 5

    a_list = Heap.rm_root(a_list)
    assert a_list[0] == 9

    a_list = Heap.rm_root(a_list)
    assert a_list == []

def test_replace_root():
    a_list = [3, 1, 5, 2, 9]
    Heap.heapify(a_list)

    Heap.replace_root(a_list, -1)
    assert a_list[0] == -1

    Heap.replace_root(a_list, 10)
    assert a_list[0] == 2

def test_add():
    a_list = [3, 1, 5, 2, 9]
    Heap.heapify(a_list)

    Heap.add(a_list, -10)
    assert a_list[0] == -10

    Heap.add(a_list, 2)
    assert a_list[0] == -10