'''


'''
import sys 
from collections import deque
input = sys.stdin.readline 
n,m = map(int,input().split())
graph = []
num = 0 
cnt = 0 

visited= [[0]*(m) for _ in range(n)]
for i in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(i,j):
    q = deque()
    q.append((i,j))
    cnt = 1 
    visited[i][j] = 1 
    while q : 
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and graph[nx][ny] == 1 : 
                visited[nx][ny] = 1 
                cnt += 1
                q.append((nx,ny))
    return cnt

                

    


for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and graph[i][j] == 1:
            num += 1 
            cnt = max(cnt,bfs(i,j))

print(num)
print(cnt)