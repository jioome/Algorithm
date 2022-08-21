from collections import * 
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        Q = [(0,k)]
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        dist = defaultdict(int)
        while Q : 
            time,node = heapq.heappop(Q)
            if node not in dist : 
                dist[node] = time
                for v,w in graph[node] : 
                    heapq.heappush(Q,(w+time,v))
        if len(dist) == n :
            return max(dist.values())
        return -1 
            