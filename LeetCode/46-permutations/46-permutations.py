from itertools import * 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [] 
        p = list(permutations(nums,len(nums)))
        print(p)
        return p 
        