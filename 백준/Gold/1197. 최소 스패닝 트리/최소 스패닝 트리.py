"""
1. 아이디어
- MST,외우기 
- 간선을 인접 리스트에 집어 넣기 
- 힙에 시작점 넣기 
- 힙이 빌 때 까지 다음의 작업을 반복
- 힙의 최소값 꺼내서, 해당 노드 방문 안했다면
- 방문표시, 해당 비용 추가 

2. 시간 복잡도 
eloge

젤 중요한 것 / MST 인지 알아보는 법 
1. 모든 노드가 연결되도록 한다. 
2. 이미 연결된 노드를 최소의 비용으로 줄이기 


"""
import sys
import heapq
input = sys.stdin.readline
v,e = map(int,input().split())
edge = [[] for _ in range(v+1)]
for i in range(e):
    a,b,c = map(int,input().split())
    edge[a].append((c,b))
    edge[b].append((c,a))
q= []
visited = [0]*(v+1)
heapq.heappush(q,(0,1))
result = 0 
while q : 
    w, node = heapq.heappop(q)
    if visited[node]== 0 : 
        result += w
        visited[node] = 1
        for next_node in edge[node]:
            if visited[next_node[1]] == 0 : 
                heapq.heappush(q,next_node)


print(result)

