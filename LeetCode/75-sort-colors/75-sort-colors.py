class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r,w,b = 0,0,len(nums)
        while w < b : 
            if nums[w] < 1 : 
                nums[r],nums[w] = nums[w],nums[r]
                w += 1 
                r += 1 
                
            elif nums[w]> 1 : 
                b-= 1
                nums[w],nums[b] = nums[b] ,nums[w]
                
                
            
            else : 
                w += 1 
        return nums