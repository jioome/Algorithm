from collections import deque
import sys
input = sys.stdin.readline 
m,n = map(int,input().split())

box = [list(map(int,input().split())) for _ in range(n)]
queue = deque()
answer = 0 
for i in range(n):
    for j in range(m):
        if box[i][j] == 1 : # 1 부터 시작 
            queue.append((i,j))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while queue : 
    x,y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0 : 
            box[nx][ny] = box[x][y] + 1 
            queue.append((nx,ny))
        

# 0 이 남아 있으면 -1 출력 
for i in box : 
    if 0 in i : 
        answer = -1
        print(-1)
        break
    else : 
        answer = max(answer,max(i))


if answer != -1 : 
    print(answer-1)