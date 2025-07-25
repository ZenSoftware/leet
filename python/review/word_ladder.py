from typing import List
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        adjacent = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                adjacent[pattern].append(word)
        
        visited = set([beginWord])
        queue = deque([beginWord])
        count = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return count
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    for adj in adjacent[pattern]:
                        if adj != word and adj not in visited:
                            queue.append(adj)
                            visited.add(adj)
            count += 1
        return 0