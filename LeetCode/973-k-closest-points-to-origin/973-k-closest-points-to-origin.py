class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = [] 
        result = [] 
        for i,v in enumerate(points) : 
            dis.append((v[0]**2 + v[1] **2 ,i))
            
        dis.sort()
        for i in range(k) : 
            idx = dis[i][1]
            result.append(points[idx])
        return result