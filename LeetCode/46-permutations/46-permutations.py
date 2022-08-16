from itertools import *

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [] 
        for i in list(permutations(nums,len(nums))):
            result.append(i)
            
        return result