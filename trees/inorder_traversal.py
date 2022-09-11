# Definition for a binary tree node.
# TC : O(N) , SC : O(N)
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root == None :
            return []
        
        if root :
            ans = self.inorderTraversal(root.left)    # Left
            ans.append(root.val)                      # Data
            ans += self.inorderTraversal(root.right)  # Right
        return ans                
        