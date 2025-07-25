# https://leetcode.com/problems/longest-absolute-file-path/description/
from typing import List

class Directory:
    def __init__(self, name: str, parent: 'Directory', depth: int):
        self.name = name.strip('\t')
        self.parent = parent
        self.depth = depth
        self.children = []

class File:
    def __init__(self, name: str):
        self.name = name.strip('\t')

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        root = self._build(input)
        result = 0
        def dfs(path: List[Directory | File]):
            nonlocal result

            if isinstance(path[-1], File):
                path_len = 0
                for item in path:
                    path_len += len(item.name)
                path_len += len(path) - 2 # add number of forward slashes
                result = max(result, path_len)
                return
            
            for p in path[-1].children:
                path.append(p)
                dfs(path)
                path.pop()

        dfs([root])
        return result

    def _build(self, input: str) -> Directory:
        input = input.split('\n')
        root = Directory('', None, -1)
        dir = root
        for item in input:
            item_depth = self._get_depth(item)
            if dir.depth+2 == item_depth:
                dir = dir.children[-1]
            else:
                while dir.depth+1 > item_depth:
                    dir = dir.parent

            if self._is_file(item):
                dir.children.append(File(item))
            else:
                dir.children.append(Directory(item, dir, dir.depth+1))

        return root
        
    def _get_depth(self, subpath: str) -> int:
        for i, c in enumerate(subpath):
            if c != '\t':
                return i
    
    def _is_file(self, subpath: str) -> int:
        return '.' in subpath