import pytest
from dsa.linkedlist import LinkedList 
from dsa.linkedlist import LinkedStack

@pytest.fixture
def empty_ll():
    return LinkedList([])

def test_linked_list_to_list(empty_ll):
    converted_list = LinkedList([1, 2, 3]).to_list()
    assert [1, 2, 3] == converted_list
    assert empty_ll.to_list() == []
    
def test_linked_list_reverse(empty_ll):
    input_list = [1, 2, 3]
    ll = LinkedList(input_list)
    ll.reverse()
    assert ll.to_list() == [3, 2, 1]
    
    empty_ll.reverse()
    assert empty_ll.to_list() == []

def test_even_odd_switch():
    input_list = [1, 2, 3]
    ll = LinkedList(input_list)
    ll.even_odd_switch()
    assert ll.to_list() == [1, 3, 2]

def test_delete():
    input_list = [1, 2, 3]
    ll = LinkedList(input_list)
    assert ll.delete(2)
    assert not ll.delete(10)
    assert ll.to_list() == [1, 3]
    assert ll.delete(1)
    assert ll.delete(3)
    assert ll.to_list() == []

def test_middle(empty_ll):
    input_list = [1, 2, 3]
    ll = LinkedList(input_list)
    assert ll.middle() == 2

    ll = LinkedList([1, 2, 3, 4])
    assert ll.middle() == 2

    assert empty_ll.middle() is None

def test_linkedstack():
    ls = LinkedStack()
    ls.push(1)
    ls.push(2)
    ls.push(3)
    assert ls.to_list() == [3, 2, 1]
    assert ls.pop() == 3
    assert ls.to_list() == [2, 1]
    assert ls.pop() == 2
    assert ls.pop() == 1
    assert ls.pop() is None
    assert ls.to_list() == []

def test_reverse_kgroup():
    ll = LinkedList([1, 2, 3])
    ll.reverse_kgroup(k = 2)
    assert ll.to_list() == [2, 1, 3]

def test_alter_merge():
    ll1 = LinkedList([1, 2, 3])
    ll2 = LinkedList([1, 2])
    ll1.alter_merge(ll2)
    assert ll1.to_list() == [1, 1, 2, 2, 3]
    assert ll2.to_list() == []

def test_concat(empty_ll):
    ll1 = LinkedList([1, 2, 3])
    ll2 = LinkedList([4, 5, 6])

    ll1.concat(ll2)
    assert ll1.to_list() == [1, 2, 3, 4, 5, 6]
    ll1.concat(empty_ll)
    assert ll1.to_list() == [1, 2, 3, 4, 5, 6]
