import sys
input = sys.stdin.readline

r,c = map(int,input().split())
board = [list(input()) for _ in range(r)]
# 시간 초과 때문에 set 사용
check = set()
ans = 0 
# 몇 칸 갈 수 있는지
result = []
def dfs(x,y,cnt):
    global ans
    ans = max(ans,cnt)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c  : 
            if board[nx][ny] not in check:
                check.add(board[nx][ny])
                dfs(nx,ny,cnt+1)
                check.remove(board[nx][ny])

        
check.add(board[0][0])
dfs(0,0,1)
print(ans)
