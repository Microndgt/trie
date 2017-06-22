END_OF = '#'


class Node(object):
    def __init__(self, depth, parent, val=None):
        self.val = val
        self.depth = depth
        self.parent = parent
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = Node(depth=0, parent=None)
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
            res.append(node.val or "root")
            stack.extend(list(node.children.values()))
        return res

    def bfs(self):
        queue = [self.root]
        res = []
        while queue:
            node = queue.pop(0)
            res.append(node.val or "root")
            queue.extend(list(node.children.values()))
        return res

    def traverse(self):
        '''
        return all words in the tree
        :return:
        '''
        pass

    def find(self, key):
        if not self.root.children:
            return
        if not key:
            return
        key += END_OF
        return self.find_node(self.root, key)

    def find_node(self, node, target):
        if not node:
            return
        if target == END_OF:
            return node
        node = node.children.get(target[0])
        if not node:
            return
        target = target[1:]
        return self.find_node(node, target)

    def remove(self, key):
        node = self.find(key)
        if not node:
            return False
        while node.val:
            cur_node = node
            node = node.parent
            if len(cur_node.children) <= 1:
                if len(node.children) > 1:
                    node.children.pop(cur_node.val)
                    break
        return True

if __name__ == "__main__":
    trie = Trie()
    trie.add("test")
    trie.add("text")
    print(trie.dfs())
    print(trie.bfs())
    print(trie.find("text").parent.parent.val)
    print(trie.remove("text"))
    print(trie.find("text"))
    print(trie.dfs())





