from ..trie import Trie

def test_insert_search():
    a_trie = Trie()
    a_trie.insert('abc')
    a_trie.insert('abe')

    search_r1 = a_trie.search('abc')
    assert search_r1[0]
    assert search_r1[1] is None

    search_r2 = a_trie.search('abf')
    assert not search_r2[0]
    assert search_r2[1] is None

    a_trie.insert('abc', 12)
    search_r3 = a_trie.search('abc')
    assert search_r3[0]
    assert search_r3[1] == 12