
import sys 

n = int(input())

answer = [] 
board = [list(map(int,input())) for _ in range(n)]
    

visited = [[0]*(n) for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def dfs(i,j):
    global cnt
    cnt += 1 
    for z in range(4):
        nx = i + dx[z]
        ny = j + dy[z]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] == 1:
            visited[nx][ny]= 1 
            dfs(nx,ny)
    return cnt

    

    

    
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and board[i][j] == 1:
            visited[i][j] = 1 
            cnt = 0 
            answer.append(dfs(i,j))

print(len(answer))
answer.sort()
for a in answer : 
    print(a)