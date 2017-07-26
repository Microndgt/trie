![https://img.shields.io/badge/Python-3-green.svg](https://img.shields.io/badge/Python-3-green.svg)

Trie
====

Data structure and relevant algorithms for extremely fast prefix/fuzzy string searching in Python.

![Trie](http://7xq6lu.com1.z0.glb.clouddn.com/trie.png)

Usage
=====

Node
----

- val
- children
- parent
- depth

Trie
----

- Get Trie size:

```
trie.size
```

- Create Trie:

```
trie = Trie()
```

- Add key:

```
trie.add("test")
```

- Remove key:

```
trie.remove("test")
```

- Find key:

```
trie.find("test")
```

- Dfs search:

```
trie.dfs()
```

- Bfs search:

```
trie.bfs()
```

- Traverse all tree

```
trie.traverse()
```

- Prefix Search(if does not have this prefix, then return all value of tree)

```
trie.prefix_search("te")
```

- Fast test for valid prefix:

```
trie.has_key_with_prefix("t")
```

- get prefix of the word

```
trie.get_prefix("testing")  # 返回test
```

- Cmp tree

```
trie1 == trie2
trie1 > trie2
trie1 < trie2
```

- If item in trie

```
"test" in trie
```

- Most used alphabet(property)

```
trie.most_used_alphabet
```

- Least used alphabet(property)

```
trie.least_used_alphabet
```

- Alphabet count

```
trie.alphabet_count()
```

To do
-----

- Fuzzy search

```
trie.fuzzy_search('es')
```

- Longest word(property)

```
trie.longest_word
```

- Shortest word(property)

```
trie.shortest_word
```

- Testing Case(Big data)

Author
======

[SkyRover](http://skyrover.me)

