from dsa.linkedlist import LinkedList 


def test_linked_list_to_list():
    input_list = [1, 2, 3]
    converted_list = LinkedList(input_list).to_list()
    assert input_list == converted_list

