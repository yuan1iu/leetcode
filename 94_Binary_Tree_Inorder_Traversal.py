# 94. Binary Tree Inorder Traversal

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder_traverse(node):
            if not node:
                return node
            inorder_traverse(node.left)
            order.append(node.val)
            inorder_traverse(node.right)

        order = []
        if root:
            inorder_traverse(root)
        return order

    def inorderTraversal_iterative(self, node):
        stack = []
        res = []
        while root or len(stack) > 0:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res
