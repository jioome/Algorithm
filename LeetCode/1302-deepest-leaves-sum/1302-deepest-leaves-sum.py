# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.ans = 0 
        self.depth = 0 
        
        def find(root,height):
            if not root : 
                return 
            if not root.left and not root.right : 
                if self.depth < height : 
                    self.depth = height
                    self.ans = root.val

                elif self.depth == height : 
                    self.ans += root.val

            find(root.left,height+1)
            find(root.right,height+1)
                
        
        find(root,1)
        return self.ans