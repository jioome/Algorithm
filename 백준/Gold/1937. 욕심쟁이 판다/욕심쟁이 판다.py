import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
# dfs, dp 같이 쓰는 문제 
dp = [[0]*(n+1) for _ in range(n+1)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]
ans = 0 

def dfs(x,y):
    # 이미 한번 왔다간 경로는 그대로 리턴
    if dp[x][y]:
        return dp[x][y]
    # 최소 하루는 살 수 있음 
    dp[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상하좌우 중에 젤 큰 거 
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny]> board[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx,ny)+1)

    return dp[x][y]





for i in range(n):
    for j in range(n):
        ans = max(ans,dfs(i,j))

print(ans)
