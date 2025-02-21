# https://leetcode.com/problems/word-search-ii/
from typing import List

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.terminal = None

class Trie:
    def __init__(self, words: List[str]):
        self.root = TrieNode(None)
        for word in words:
            node = self.root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.terminal = word

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        trie = Trie(words)
        result, visited = set(), set()

        def scan(r: int, c: int, node: TrieNode):
            if r not in range(rows):
                return
            if c not in range(cols):
                return
            if (r,c) in visited:
                return
            if board[r][c] not in node.children:
                return
            
            next_node = node.children[board[r][c]]
            if next_node.terminal:
                result.add(next_node.terminal)

            visited.add((r,c))

            scan(r-1, c, next_node)
            scan(r+1, c, next_node)
            scan(r, c-1, next_node)
            scan(r, c+1, next_node)

            visited.remove((r,c))
        
        for r in range(rows):
            for c in range(cols):
                scan(r, c, trie.root)
        
        return list(result)