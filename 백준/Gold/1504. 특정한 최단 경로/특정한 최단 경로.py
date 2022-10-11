import sys,heapq
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,e = map(int,input().split())
graph = [[]*(n+1) for _ in range(n+1)]

# 양방향 그래프 만들기
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1,v2 = map(int,input().split())


def dijkstra(start,end):
    dis = [float('inf')]*(n+1)
    dis[start] = 0 
    q =[]
    heapq.heappush(q,(0,start))

    while q : 
        # 거리, 현재 정점
        k,u = heapq.heappop(q)

        if k > dis[u]:
            continue
        for w,v in graph[u]:
            if dis[w] > dis[u] + v : 
                dis[w] = dis[u] + v
                heapq.heappush(q,(dis[w],w))
    # 도착할 때 걸리는 거리 
    return dis[end]



# 만들어질 수 있는 두 가지의 경로의 수 중에 최단 거리 
path1 = dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,n)
path2 = dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,n)
if path1 == float('inf') and path2== float('inf'):
    print(-1)
else : 
    print(min(path1,path2))
