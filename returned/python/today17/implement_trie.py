# https://leetcode.com/problems/implement-trie-prefix-tree/

class Node:
    def __init__(self, val: str):
        self.val = val
        self.children = dict()
        self.is_terminal = False

class Trie:

    def __init__(self):
        self.root = Node(None)

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node(c)
            node = node.children[c]
        node.is_terminal = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_terminal

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True