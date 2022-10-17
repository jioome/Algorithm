class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [] 
        lst = [] 
        def dfs(elements):
            if len(elements) == 0 : 
                return result.append(lst[:])
            for e in elements : 
                nex = elements[:]
                nex.remove(e)
                lst.append(e)
                dfs(nex)
                lst.pop()
        dfs(nums)        
        return result
        