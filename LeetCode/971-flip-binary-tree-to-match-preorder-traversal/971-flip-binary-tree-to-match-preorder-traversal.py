# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
            if not node:
                return True

            if node.val != self.voyage[self.i]:
                print(node.val,self.voyage[self.i])
                return False

            self.i += 1

            if node.left and node.left.val != self.voyage[self.i]:
                node.left, node.right = node.right, node.left
                self.ans.append(node.val)

            return self.dfs(node.left) and self.dfs(node.right)
    
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        self.voyage = voyage
        self.i = 0
        self.ans = []
        return self.ans if self.dfs(root) else [-1]
        
