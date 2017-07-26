import unittest
from copy import deepcopy
from trie import Trie


class TestTrie(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()
        self.words = ['text', 'test', 'world', 'hello']
        self.alphabets = ['root', 't', 'e', 'x', 't', '#', 's', 't', '#', 'w', 'o', 'r', 'l', 'd', '#', 'h', 'e', 'l', 'l', 'o', '#']
        self.alphabet_count = {'t': 3, 'e': 2, 'x': 1, 'd': 1, 's': 1, 'o': 2, 'r': 1, 'h': 1, 'l': 3, 'w': 1}
        for word in self.words:
            self.trie.add(word)

    def test_equal(self):
        trie2 = deepcopy(self.trie)
        self.assertEqual(trie2, self.trie)
        trie2.add('a')
        self.assertNotEqual(trie2, self.trie)

    def test_add(self):
        res = self.trie.traverse()
        for word in self.words:
            self.assertTrue(word in res)

        for r in res:
            self.assertTrue(r in self.words)

    def test_find(self):
        self.assertTrue(self.trie.find('test'))
        self.assertEqual(None, self.trie.find("testing"))

    def test_prefix_search(self):
        res = self.trie.prefix_search('')
        for word in self.words:
            self.assertTrue(word in res)

        for r in res:
            self.assertTrue(r in self.words)

        self.assertEqual(['test'], self.trie.prefix_search('tes'))

    def test_tranverse(self):
        dfs_res = self.trie.dfs()
        for al in self.alphabets:
            self.assertTrue(al in dfs_res)

        for dr in dfs_res:
            self.assertTrue(dr in self.alphabets)

        bfs_res = self.trie.bfs()
        for al in self.alphabets:
            self.assertTrue(al in bfs_res)

        for br in bfs_res:
            self.assertTrue(br in self.alphabets)

    def test_contains(self):
        self.assertTrue('text' in self.trie)
        self.assertFalse('testing' in self.trie)

    def test_alphabets(self):
        self.assertEqual(self.alphabet_count, self.trie.alphabet_count())
        self.assertTrue(self.trie.most_used_alphabet in [('t', 3), ('l', 3)])
        self.assertTrue(self.trie.least_used_alphabet in [('w', 1), ('d', 1), ('s', 1), ('r', 1), ('h', 1), ('x', 1)])

    def test_get_prefix(self):
        self.assertEqual('test', self.trie.get_prefix('testing'))
        self.assertEqual('doing', self.trie.get_prefix('doing'))

        dtrie = Trie()

        for wd in ["cat", "bat", "rat"]:
            dtrie.add(wd)

        self.assertEqual('bat', dtrie.get_prefix("battle"))
        self.assertEqual('was', dtrie.get_prefix('was'))

if __name__ == "__main__":
    unittest.main()
