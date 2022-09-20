from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        index = bisect_left(nums,target)
        if target not in nums : 
            return -1

        return index