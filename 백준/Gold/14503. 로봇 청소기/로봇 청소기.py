import sys
input = sys.stdin.readline 
'''
- 현재 위치 청소 
- 왼쪽 탐색
- 모두 청소 되어 있는 경우 후진
- 후진 했는데 벽이면 멈춘다. 

구현 
'''

n,m = map(int,input().split())
r,c,d = map(int,input().split())
dx= [-1,0,1,0]
dy = [0,1,0,-1]
board = []
for i in range(n):
    board.append(list(map(int,input().split())))


cnt = 1
board[r][c] = 2
while True : 
    check = False 
    for i in range(4):
        nx = r + dx[(d+3)%4]
        ny = c + dy[(d+3)%4]
        d = (d+3)%4
        if 0 <= nx < n and 0 <= ny < m : 
            if board[nx][ny] == 0 : 
                cnt += 1 
                board[nx][ny] =2 
                r = nx
                c= ny
                check = True 
                break
    if check == False : 
        nx = r - dx[d]
        ny = c - dy[d]
        r = nx
        c = ny
        if board[nx][ny] == 1 : 
            print(cnt)
            break
