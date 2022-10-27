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

heapq.heappush(q,(0,1))
chk = [0]*(v+1)
result = 0
while q : 
    w,node = heapq.heappop(q)
    if chk[node] == 0  : 
        chk[node] = 1
        result += w
        for next_edge in edge[node]:
            if chk[next_edge[1]] == 0:
                heapq.heappush(q,next_edge)
print(result)




