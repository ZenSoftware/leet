# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
from collections import deque
from typing import Optional

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return ''
        
        levels = []
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)
        
        with_nulls = [[str(root.val)]]
        for i in range(len(levels)-1):
            level = levels[i]
            show_nulls = False
            with_nulls_level = []
            for n in reversed(level):
                if n.right:
                    with_nulls_level.append(str(n.right.val))
                    show_nulls = True
                elif show_nulls:
                    with_nulls_level.append('null')
                
                if n.left:
                    with_nulls_level.append(str(n.left.val))
                    show_nulls = True
                elif show_nulls:
                    with_nulls_level.append('null')
            with_nulls_level.reverse()
            with_nulls.append(with_nulls_level)
        
        stringified_levels = []
        for level in with_nulls:
            stringified_levels.append(','.join(level))
        
        return '|'.join(stringified_levels)

    def deserialize(self, data):
        if not data:
            return None

        levels = []
        string_levels = data.split('|')
        for string_level in string_levels:
            string_level = string_level.split(',')
            level = []
            for n in string_level:
                parsed = None if n == 'null' else TreeNode(int(n))
                level.append(parsed)
            levels.append(level)
        
        for row in range(len(levels)-1):
            i = 0
            for node in levels[row]:
                if node:
                    if i in range(len(levels[row+1])):
                        node.left = levels[row+1][i]
                        i += 1
                    if i in range(len(levels[row+1])):
                        node.right = levels[row+1][i]
                        i += 1
        
        return levels[0][0]