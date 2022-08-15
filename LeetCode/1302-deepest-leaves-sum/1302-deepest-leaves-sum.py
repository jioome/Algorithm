# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        ans = 0 
        depth = 0 
        
        def find(root,height):
            nonlocal ans
            nonlocal depth
            if not root : 
                return 
            if not root.left and not root.right : 
                if depth < height : 
                    depth = height
                    ans = root.val
                elif depth == height : 
                    ans += root.val
                return 
            find(root.left,height+1)
            find(root.right,height+1)
                
        
        find(root,1)
        return ans