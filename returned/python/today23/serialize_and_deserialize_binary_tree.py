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
        
        withNulls = [[str(root.val)]]
        for i in range(len(levels)-1):
            level = levels[i]
            showNulls = False
            withNullsLevel = []
            for n in reversed(level):
                if n.right:
                    withNullsLevel.append(str(n.right.val))
                    showNulls = True
                elif showNulls:
                    withNullsLevel.append('null')
                
                if n.left:
                    withNullsLevel.append(str(n.left.val))
                    showNulls = True
                elif showNulls:
                    withNullsLevel.append('null')
            withNullsLevel.reverse()
            withNulls.append(withNullsLevel)
        
        stringified = []
        for level in withNulls:
            stringified.append(','.join(level))
        
        return '|'.join(stringified)

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