import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = [] 
        for (x,y) in points:
            heapq.heappush(heap,(x**2 + y**2 , x,y))
        
        for i in range(k) : 
            dis,x,y = heapq.heappop(heap)
            result.append((x,y))
        return result
            
            