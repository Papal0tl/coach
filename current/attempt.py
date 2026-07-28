"""
User attempt for Construct Binary Tree from Preorder and Inorder Traversal.

Write your reasoning in English comments when useful.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        idx = inorder.index(root.val)
        root.left = self.buildTree()
        root.right = self.buildTree()
        return root