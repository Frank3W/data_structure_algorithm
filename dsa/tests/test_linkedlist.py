from dsa.linkedlist import LinkedList 


def test_linked_list_to_list():
    input_list = [1, 2, 3]
    converted_list = LinkedList(input_list).to_list()
    assert input_list == converted_list
    assert LinkedList([]).to_list() == []
    
def test_linked_list_reverse():
    input_list = [1, 2, 3]
    ll = LinkedList(input_list)
    ll.reverse()
    assert ll.to_list() == [3, 2, 1]
    
    ll_null = LinkedList([])
    ll_null.reverse()
    assert ll_null.to_list() == []

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
