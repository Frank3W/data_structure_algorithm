from ..dynamicprogramming import FibMem

def test_fibmem():
    a_fibmem = FibMem(10)

    assert a_fibmem.get_value(5) == 5
    assert a_fibmem.get_value(6) == 8
    assert a_fibmem.get_value(7) == 13