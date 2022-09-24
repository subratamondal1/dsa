# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base Condition:
        # Return the minimum valid input i.e node == null
        # Hypothesis :
        # Find height of Left Subtree of a node
        # Find height of Right Subtree of a node
        # Induction :
        # Add 1 to the max of left or right subtree

        # Base Condition
        if root == None:
            return 0

        # Hypothesis
        left_subtree_height = self.maxDepth(root.left)
        right_subtree_height = self.maxDepth(root.right)

        # Induction
        return 1 + max(left_subtree_height, right_subtree_height)
