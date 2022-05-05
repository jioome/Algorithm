from collections import deque
import sys




input = sys.stdin.readline 
q = deque()
f,s,g,u,d = map(int,input().split())

def bfs() :
    q.append(s)
    visited = [0]*(f+1)
    visited[s] = 1
    while q : 
        x = q.popleft()
        if x == g :
            return visited[g]-1
        dx = [u,-d]
        for i in range(2):
            nx = x + dx[i]
            if 1 <= nx <= f and visited[nx] == 0:
                q.append(nx)
                visited[nx] = visited[x]+1
    return "use the stairs"
print(bfs()) # 1층에서 visited[s] = 1 이므로 1을 빼준다. 


