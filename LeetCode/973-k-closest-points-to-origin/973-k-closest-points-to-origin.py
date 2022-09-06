import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = [] 
        answer = [] 
        for a,b in points :
            print(a,b)
            cnt = a**2 + b **2
            heapq.heappush(q,(cnt,a,b))
        
        for _ in range(k) :
            cnt,a,b = heapq.heappop(q)
            answer.append((a,b))
        return answer
        
    