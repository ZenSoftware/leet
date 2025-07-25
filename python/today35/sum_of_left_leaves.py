# https://leetcode.com/problems/sum-of-left-leaves/description/
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Time: O(n) due to a DFS traversal, visiting all nodes just once
    Space: O(log(n)) height of tree is log(n), thus
           max size of recursive stack frames will be log(n).
           Each stack frame containing constant space.
    '''
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        if root.left and not root.left.left and not root.left.right:
            ans = root.left.val
        ans += self.sumOfLeftLeaves(root.left)
        ans += self.sumOfLeftLeaves(root.right)
        return ans