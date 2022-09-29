from collections import deque
n,m  = map(int,input().split())
board = [list(map(int,input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

q = deque()
def bfs(a,b) : 
    dx = [ -1,1,0,0]
    dy = [0,0,1,-1]
    q.append((a,b))
    visited[a][b] = 1 
    while q : 
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if  0<= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1 
                q.append((nx,ny))
            

bfs(0,0)
print(board[n-1][m-1])

from collections import deque
n,m  = map(int,input().split())
board = [list(map(int,input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

# 최소, 최단이라는 말이 나오면 일단 bfs 먼저 생각
# bfs 이기 때문에 deque를 사용 
# visitied 배열로 방문 처리 

q = deque()
def bfs(a,b) : 
    dx = [ -1,1,0,0]
    dy = [0,0,1,-1]
    q.append((a,b))
    visited[a][b] = 1 
    while q : 
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if  0<= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1 
                q.append((nx,ny))
            

bfs(0,0)
print(board[n-1][m-1])


'''
4 6
101111
101010
101011
111011


=>15
'''
