# 230. Kth Smallest Element in a BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:  # recursive
        def inorder(node, node_list):
            if not node:
                return node
            inorder(node.left, node_list)
            node_list.append(node)
            inorder(node.right, node_list)
        node_list = []
        if root:
            inorder(root, node_list)
        return node_list[k-1].val
