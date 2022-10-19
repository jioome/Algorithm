import sys
from collections import deque
# c가 크니까 이분탐색 해야함
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

def bfs(mid) : 
    visited[start] = 1
    q = deque()
    q.append(start)
    while q : 
        now = q.popleft()
        if now == end : 
            return True 
        for nx,nc in graph[now]:
            # 갈 수 있으면서 무게 제한에 걸리지 않는 경우
            if visited[nx] == 0 and mid <= nc : 
                q.append(nx)
                visited[nx] = 1 
    return False

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for i in range(1, n + 1):
    graph[i].sort(reverse=True)

start, end = map(int, input().split())
low, high = 1, 1000000000
result = low
while low <= high:
    visited = [0 for _ in range(n + 1)]
    mid = (low + high) // 2
    if bfs(mid): 
        # 목적지까지 도달이 가능하다면 low를 올림
        # 값을 저장하고 최댓값을 구하기 위해 low 값을 올린다
        result= mid
        low = mid + 1
    else: # 목적지까지 불가능하다면 high를 내림
        high = mid - 1

print(result)