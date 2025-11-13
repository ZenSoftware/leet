from collections import defaultdict


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findFrequentTreeSum(self, root):
        if not root:
            return []

        subtree_sums = {}

        def dfs(node):
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

            subtree_sums[node] = node.val
            if node.left:
                subtree_sums[node] += subtree_sums[node.left]
            if node.right:
                subtree_sums[node] += subtree_sums[node.right]

        dfs(root)

        sum_counts = defaultdict(int)
        for s in subtree_sums.values():
            sum_counts[s] += 1

        largest = 0
        result = []
        for s, count in sum_counts.items():
            if count > largest:
                result = [s]
                largest = count
            elif count == largest:
                result.append(s)

        return result
