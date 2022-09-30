import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
high = 0
result = [] 
# 제일 큰 값 구하기 
for i in range(n):
    high = max(high,max(board[i]))


def dfs(x,y,r):
    visited[x][y] = 1
    dx =[-1,1,0,0]
    dy =[0,0,1,-1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > r and visited[nx][ny] == 0 :
            dfs(nx,ny,r)

# r은 빗물의 높이 
for r in range(high):
    visited = [[0]*n for _ in range(n)]
    cnt = 0 
    for i in range(n):
        for j in range(n):
            if board[i][j] > r and visited[i][j] == 0 :
                cnt += 1 
                dfs(i,j,r)
    result.append(cnt)

print(max(result))
