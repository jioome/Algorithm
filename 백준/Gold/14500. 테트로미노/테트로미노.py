import sys ,heapq
input = sys.stdin.readline 

n,m = map(int,input().split())
board = []

for i in range(n):
    board.append(list(map(int,input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
max_val = max(map(max,board))
answer = 0
def dfs(x,y,l,sum_n):
    global answer
    if answer >= sum_n + max_val*(3-l):
        return 
    if l == 3 : 
        answer  = max(answer,sum_n)
        return 
    
    else: 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i] 
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]==0 : 
                if l == 1 : 
                    visited[nx][ny] = 1
                    dfs(x,y,l+1,sum_n+ board[nx][ny])
                    visited[nx][ny] = 0
                
                visited[nx][ny] = 1
                dfs(nx,ny,l+1,sum_n+ board[nx][ny])
                visited[nx][ny] = 0
visited =[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i,j,0,board[i][j])
        visited[i][j] = 0 
print(answer)


