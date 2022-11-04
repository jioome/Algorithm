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
        dis = (d+3)%4
        nx = r + dx[dis]
        ny = c + dy[dis]
        d = (d+3)%4
        if 0 <= nx < n and 0 <= ny < m : 
            if board[nx][ny] == 0 : 
                board[nx][ny] = 2
                cnt += 1
                check = True 
                r,c= nx ,ny
                break
    if check == False : 
        
        if board[r - dx[d]][c - dy[d]] ==  1 : 
            print(cnt)
            break
        else : 
            r,c = r - dx[d] ,c - dy[d]
    
        

