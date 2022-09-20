class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0 
        end = len(numbers)-1

        while start <=end : 
            add_ = numbers[start] + numbers[end]
            print(add_)
            if add_ < target : 
                start = start + 1
            elif add_ > target :
                end = end -1
            else : 
                return [start+1,end+1]
            
        