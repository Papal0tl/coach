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
        self.length = 0
        def getDepth(node):
            if node is None:
                return 0
            left_depth = getDepth(node.left)
            right_depth = getDepth(node.right)
            cur_length = left_depth + right_depth
            self.length = max(self.length, cur_length)
            return 1 + max(left_depth, right_depth)
        getDepth(root)
        return self.length

