"""
User attempt for Diameter of Binary Tree.

Write your reasoning in English comments when useful.
"""


class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        length = 0
        def getDepth(self, node):
            if node is None:
                return 0
            left_depth = getDepth(node.left)
            right_depth = getDepth(node.right)
            length = left_depth + right_depth
            return length
        getDepth(root)
        return length

