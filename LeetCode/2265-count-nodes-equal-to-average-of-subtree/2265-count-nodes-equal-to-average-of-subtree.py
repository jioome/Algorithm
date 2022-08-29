# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def rec(node, counter, sum_):
            nonlocal ans 
            if node is None : 
                return counter,sum_
            
            if not node.left and not node.right : 
                ans+=1 
                return counter+1, sum_+ node.val
            
            left_counter, left_sum = rec(node.left, counter, sum_)
            right_counter, right_sum = rec(node.right, counter, sum_)
            sum_ = left_sum + right_sum + node.val
            counter = left_counter + right_counter + 1
            if sum_ // counter == node.val:
                ans += 1
            return counter, sum_
            
        rec(root,0,0)
        return ans