from collections import deque
import sys

input = sys.stdin.readline 

t = int(input())
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs():
    cnt = 0 # 시간 
    while q : 
        cnt += 1 
        # 불이 먼저 번지도록 한다
        while f and f[0][2] < cnt:
            x, y, time = f.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if building[nx][ny] == "." or building[nx][ny] == "@":
                        building[nx][ny] = "*"
                        f.append((nx, ny, time + 1))

        while q and q[0][2] < cnt:
            x, y, time = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if building[nx][ny] == "." and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny, time + 1))
                else: # 예외 조건 위치 잘 생각하기 
                    return cnt

    return "IMPOSSIBLE"


for _ in range(t):
    w,h = map(int,input().split())
    building = [list(input()) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    q = deque()
    f = deque() # 불의 위치 

    for i in range(h) : 
        for j in range(w) : 
            if building[i][j] == '@' : 
                visited[i][j] = 1
                q.append((i,j,0))
            elif building[i][j] == '*' : 
                f.append((i,j,0))
    print(bfs())
    
                