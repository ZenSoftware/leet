# https://leetcode.com/problems/concatenated-words/description/
from typing import List
from functools import cache


class TrieNode:
    def __init__(self):
        self.terminal = False
        self.children = {}


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.terminal = True

    @cache
    def dfs(self, key: str, index: int, count: int) -> bool:
        if index >= len(key):
            return count > 1
        curr = self.root
        for i in range(index, len(key)):
            if key[i] not in curr.children:
                return False
            curr = curr.children[key[i]]
            if curr.terminal:
                if self.dfs(key, i + 1, count + 1):
                    return True
        return False

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        for word in words:
            self.insert(word)

        ans = []
        for word in words:
            if self.dfs(word, 0, 0):
                ans.append(word)
        return ans
