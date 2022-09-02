class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nume= list(enumerate(nums,0))
        print(nume)
        nume.sort(key= lambda x : x[1])
        print(nume)
        start = 0 
        end = len(nums) -1 
        while start < end :
            if nume[start][1] + nume[end][1] < target : 
                start+= 1 
            elif nume[start][1] + nume[end][1] > target :
                end -= 1
            else : 
                return [nume[start][0],nume[end][0]]
        