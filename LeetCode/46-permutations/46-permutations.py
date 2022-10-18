class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        lst = [] 
        def dfs(element):
            if len(lst) == len(nums):
                result.append(lst[:])
                return 
            for e in element :
                nxt = element[:]
                nxt.remove(e)
                lst.append(e)
                dfs(nxt)
                lst.pop()
        
        dfs(nums)
        return result