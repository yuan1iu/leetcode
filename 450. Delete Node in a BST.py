# 450. Delete Node in a BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return None
            if root.left and not root.right:
                return root.left
            if not root.left and root.right:
                return root.right
            if root.left and root.right:
                # find the minimum item of right sub tree
                min_node = root.right
                while min_node.left:
                    min_node = min_node.left
                # swap the value with the deleted node
                min_node.val, root.val = root.val, min_node.val
                # delete the node
                root.right = self.deleteNode(root.right, key)
                return root
        return root
