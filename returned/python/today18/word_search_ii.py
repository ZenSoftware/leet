# https://leetcode.com/problems/word-search-ii/
from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        
        def exists(r: int, c: int, word: str, i: int, visited: set) -> bool:
            if r not in range(rows):
                return False
            if c not in range(cols):
                return False
            if (r,c) in visited:
                return False
            if word[i] != board[r][c]:
                return False
            if i == len(word) - 1:
                return True
            
            visited.add((r,c))

            up =    exists(r-1, c, word, i+1, visited)
            down =  exists(r+1, c, word, i+1, visited)
            left =  exists(r, c-1, word, i+1, visited)
            right = exists(r, c+1, word, i+1, visited)
            
            visited.remove((r,c))

            return right or left or up or down
        
        result = []
        def scan_board(word):
            for r in range(rows):
                for c in range(cols):
                    if exists(r, c, word, 0, set()):
                        result.append(word)
                        return
                    
        for word in words:
            scan_board(word)
                        
        return result