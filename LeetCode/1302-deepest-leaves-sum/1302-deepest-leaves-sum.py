# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math 
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.ans = 0 
        self.result = 0 
        def find(root,height):
            if not root : 
                return  
            if not root.left and not root.right:
                if self.result < height :
                    self.result = height
                    self.ans = root.val
                elif  self.result == height :
                    self.ans += root.val
                return 
            
            find(root.left,height+1)
            find(root.right,height+1)
        find(root,1)
        return self.ans
