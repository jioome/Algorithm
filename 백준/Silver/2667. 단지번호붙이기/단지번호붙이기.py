import sys
sys.setrecursionlimit(10**5)
n = int(input())
board = [list(map(int,input())) for _ in range(n)]
result = []
dx = [-1,1,0,0]
dy = [0,0,1,-1]
house =0
def dfs(x,y):
    # 한 단지마다 집의 수 
    global house 
    house+= 1 
    # 값을 0으로 바꿔주면서 방문 처리 
    board[x][y] = 0 

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1: 
            dfs(nx,ny)
        
for i in range(n): 
    for j in range(n):
        if board[i][j] == 1  : 
            dfs(i,j)
            result.append(house)
            house =0
        
result.sort()
print(len(result))
for r in result : 
    print(r)
