import heapq
def solution(n, s, a, b, fares):
    '''
    s 출발 
    1. 아이디어
    다익스트라 알고리즘? 거기서 
    2. 시간 복잡도 
    3. 자료 구조 
    '''
    answer = 0
    graph = [[] for _ in range(n+1)]
    for c,d,f in fares : 
        graph[c].append((d,f))
        graph[d].append((c,f))
        
    
    def dij(start,end):
        dist = [float('inf')]*(n+1)
        dist[start] =0 
        q = [] 
        heapq.heappush(q,(0,start))
        while q : 
            w,now = heapq.heappop(q)
            if dist[now] < w : 
                continue
            for node,m in graph[now]:
                if m + dist[now] < dist[node]:
                    dist[node] = m + dist[now]
                    heapq.heappush(q,(dist[node],node))
        return dist[end]
                    
        
        
        
    
    d1 = float('inf')
    for k in range(1,n+1):
        d1 =min(d1,dij(s,k) + dij(k,a)+ dij(k,b))
    d2 = dij(s,b) + dij(s,a)
    answer =min(d1,d2)
    
    return answer