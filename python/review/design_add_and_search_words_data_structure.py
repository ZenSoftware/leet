# https://leetcode.com/problems/design-add-and-search-words-data-structure/
from typing import Dict

class Node:
    def __init__(self, val):
        self.val = val
        self.children: Dict[str, Node] = dict()
        self.terminal = False

class WordDictionary:

    def __init__(self):
        self.root = Node(None)

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node(c)
            node = node.children[c]
        node.terminal = True

    def search(self, word: str) -> bool:
        return self.dfs(word, self.root)
    
    def dfs(self, word: str, node: Node) -> bool:
        for i, c in enumerate(word):
            if c == '.':
                for _, child in node.children.items():
                    if self.dfs(word[i+1:], child):
                        return True
                return False
            elif c not in node.children:
                return False
            node = node.children[c]
        return node.terminal