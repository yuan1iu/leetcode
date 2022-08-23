# 95. Unique Binary Search Trees II
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n):
        def dfs(st, end):
            if st > end: return [None]
            if st == end: return [TreeNode(st)]
            pos = []
            for i in range(st, end+1):
                left = dfs(st, i-1)
                right = dfs(i+1, end)
                for l in range(len(left)):
                    for r in range(len(right)):
                        root = TreeNode(i, l, r)
                        pos.append(root)                       
            return pos
        return dfs(1, n)