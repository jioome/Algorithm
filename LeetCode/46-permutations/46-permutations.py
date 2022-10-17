class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result =[] 
        pre = [] 
        def dfs(nums):
            if len(nums)== 0 : 
                result.append(pre[:])
            for n in nums : 
                nex = nums[:]
                nex.remove(n)
                pre.append(n)
                dfs(nex)
                pre.pop()
        dfs(nums)
        return result