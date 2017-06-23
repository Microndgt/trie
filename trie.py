END_OF = '#'


class Node(object):
    def __init__(self, depth, parent, val=None):
        self.val = val
        self.depth = depth
        self.parent = parent
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = Node(depth=0, parent=None, val="root")
        self.size = 0

    def get_root(self):
        return self.root

    def add(self, key):
        self.size += 1
        node = self.root
        for ele in key:
            if ele not in node.children:
                node.children[ele] = Node(node.depth+1, node, ele)
            node = node.children[ele]
        else:
            node.children[END_OF] = Node(node.depth+1, node, END_OF)
        return self.root

    def dfs(self):
        stack = [self.root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(list(node.children.values()))
        return res

    def bfs(self):
        queue = [self.root]
        res = []
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            queue.extend(list(node.children.values()))
        return res

    def traverse(self):
        '''
        return all words in the tree
        :return:
        '''
        return self.prefix_search('')

    def find(self, key):
        if not self.root.children:
            return
        if not key:
            return
        key += END_OF
        return self._find_node(self.root, key)

    def _find_node(self, node, target):
        if not node:
            return
        if target == END_OF:
            return node
        node = node.children.get(target[0])
        if not node:
            return
        target = target[1:]
        return self._find_node(node, target)

    def remove(self, key):
        node = self.find(key)
        if not node:
            return False
        node.children.pop(END_OF)
        cur_node = node
        node = node.parent
        i = 1
        while len(cur_node.children) == 0 and cur_node != self.root:
            ele = key[len(key)-i]
            self._remove_child(node, ele)
            i += 1
            cur_node = node
            node = node.parent
        return True

    def _remove_child(self, node, ele):
        node.children.pop(ele)

    def prefix_search(self, key):
        node = self.find(key)
        res = []
        if not node:
            self._rec_prefix_search(self.root, '', res)
        else:
            self._rec_prefix_search(node, key, res)
        return res

    def has_key_with_prefix(self, key):
        if key == "":
            return True
        node = self.find(key)
        if not node:
            return False
        return True

    def _rec_prefix_search(self, node, word, res):
        if node.val == END_OF:
            res.append(word)
            return
        for child in node.children.values():
            if child.val != END_OF:
                self._rec_prefix_search(child, word+child.val, res)
            else:
                self._rec_prefix_search(child, word, res)

    def fuzzy_search(self, key):
        pass

if __name__ == "__main__":
    trie = Trie()
    trie.add("test")
    trie.add("text")
    print(trie.dfs())
    print(trie.bfs())
    print(trie.bfs())
    print(trie.find("test"))
    print(trie.dfs())
    print(trie.prefix_search("tes"))
    print(trie.traverse())
    print(trie.has_key_with_prefix("t"))
    print(trie.fuzzy_search('t'))





