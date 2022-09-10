
# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # TC = O(N), SC = O(N)
        # APPROACH
        
        # 1. Make a Queue and Push two element : a) Root b) None (None Helps to differentiate between levels)
        # 2. While the Queue is Not Empty
            # a) We need to pop(0) the first element and get it from the queue to store it 
            # b) Now we need to perform two checks on the popped element:
                # i) is the popped_element None ? If yes : Then perform two operations: 
                    # a) End of the Current Level , so append the elements of temp after the end of current level \
                    #   and reset temp 
                    #    so it can store only the elements of the next level: ans.append(temp)
                    # b) Push None to the queue iff the Queue is Not empty else dont push None
                # ii) is the popped_element Not None ? If yes : Then perform two operations :
                    # a) If popped_element.left exists then Push it in the Queue
                    # b) If popped_element.right exists then Push it in the Queue

        if root == None:
            return []                    
                    
        ans = []
        temp = []   # Stores result of the current level
        
        queue = []                                    # 1
        queue.append(root)
        queue.append(None)  
        
        while queue:                                  # 2
            popped_node = queue.pop(0)                # 2.a
           
            if popped_node == None:                   # 2.b.i.a
                ans.append(temp)
                temp = []                             # Reset temp for the Next Level
                if queue:                             # 2.b.i.b
                    queue.append(None)
            else:                                     # 2.b.ii
                temp.append(popped_node.val)
                if popped_node.left:                  # 2.b.ii.a
                    queue.append(popped_node.left)
                if popped_node.right:                 # 2.b.ii.b
                    queue.append(popped_node.right)
        return ans
