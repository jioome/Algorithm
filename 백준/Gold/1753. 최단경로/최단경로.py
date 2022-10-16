import sys,heapq

input = sys.stdin.readline
n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]

k = int(input())
dist = [float('inf')]*(n+1)

for _ in range(e):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

def dijkstra(start):
    q = [] 
    dist[start] = 0
    heapq.heappush(q,(0,start))
    while q : 
        d,cur = heapq.heappop(q)
        if dist[cur] < d:
            continue
        for i in graph[cur]:
            cost = d + i[1]
            if cost < dist[i[0]] : 
                dist[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))



dijkstra(k)

for i in range(1,n+1):
    if dist[i]== float('inf'):
        print("INF")
    else : 
        print(dist[i])