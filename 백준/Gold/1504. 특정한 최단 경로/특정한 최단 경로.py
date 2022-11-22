import sys ,heapq
input = sys.stdin.readline 

sys.setrecursionlimit(10**9)
'''
무방향 

'''
n,e = map(int,input().split())
graph =[[] for _ in range(n+1) ] 

for _ in range(e):
	a,b,c = map(int,input().split())
	graph[a].append((b,c))
	graph[b].append((a,c))
v1,v2 = map(int,input().split())

def dijkstra(start,end):
	dist = [float('inf')]*(n+1)
	q = []
	dist[start] = 0
	heapq.heappush(q,(0,start))
	while q : 
		d,v = heapq.heappop(q)
		if dist[v] < d : 
			continue
		for node,w in graph[v]:
			if d + w < dist[node]:
				dist[node] = d+w
				heapq.heappush(q,(dist[node],node))
	return dist[end]


path1 = dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,n)
path2 = dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,n)
if path1 == float('inf') and path2== float('inf'):
    print(-1)
else : 
    print(min(path1,path2))