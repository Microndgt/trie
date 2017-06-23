![https://img.shields.io/badge/Python-3-green.svg](https://img.shields.io/badge/Python-3-green.svg)

Trie
====

Data structure and relevant algorithms for extremely fast prefix/fuzzy string searching in Python.

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

Author
======

[SkyRover](http://skyrover.me)

