import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lst = [] 
        for n in nums : 
            heapq.heappush(lst,-n)
        answer = 0 
        for _ in range(k):
            answer = heapq.heappop(lst)
        return -answer 
            
        
            