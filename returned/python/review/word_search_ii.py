# https://leetcode.com/problems/word-search-ii/
from typing import Dict, List, Tuple

class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = dict()
        self.terminal = None

class Trie:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for word in words:
            node = self.root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.terminal = word
    
    def prune(self, word: str):
        node = self.root
        path: List[Tuple[TrieNode, str]] = []

        for child_key in word:
            path.append((node, child_key))
            node = node.children[child_key]
        
        for parent, child_key in reversed(path):
            target = parent.children[child_key]
            if len(target.children) == 0:
                del parent.children[child_key]
            else:
                return

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
            
            node = node.children[board[r][c]]
            if node.terminal:
                result.add(node.terminal)
                trie.prune(node.terminal)

            visited.add((r,c))

            scan(r-1, c, node)
            scan(r+1, c, node)
            scan(r, c-1, node)
            scan(r, c+1, node)

            visited.remove((r,c))
        
        for r in range(rows):
            for c in range(cols):
                scan(r, c, trie.root)
        
        return list(result)