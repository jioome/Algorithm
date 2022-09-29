from collections import deque
import sys
input = sys.stdin.readline 

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
q = deque()
visited = [[0]*n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]

# 거리 리스트 
distanye = [[-1] * n for _ in range(n)]

# 육지 가장자리 x,y 좌표와 육지 번호 저장
sea = deque()

# 육지 구역마다 넘버링
def numbering(board, number):
    q = deque()
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1 and visited[i][j]==0:
                q.append((i, j))
                visited[i][j] = True
                board[i][j] = number
                distanye[i][j] = 0  # 육지라서 거리 0

                while q:
                    r, c = q.popleft()
                    for d in range(4):
                        nx = r + dx[d]
                        ny = c + dy[d]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 :
                            # 육지라면 넘버링 계속 진행
                            if board[nx][ny] == 1:
                                q.append((nx, ny))
                                visited[nx][ny] = 1
                                board[nx][ny] = number  # 넘버링 진행
                                distanye[nx][ny] = 0
                            
                            # 바다라면 (가장자리라는 말과 같음)
                            # 육지의 가장자리 좌표와 육지 번호 저장
                            elif board[nx][ny] == 0:
                                sea.append((r, c, number))from collections import deque
import sys
input = sys.stdin.readline 

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
q = deque()
visited = [[0]*n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]

# 거리 리스트 
distance = [[-1] * n for _ in range(n)]

# 육지 가장자리 x,y 좌표와 육지 번호 저장
sea = deque()

# 육지 구역마다 넘버링
def numbering(board, number):
    q = deque()
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1 and visited[i][j]==0:
                q.append((i, j))
                visited[i][j] = True
                board[i][j] = number
                distance[i][j] = 0  # 육지라서 거리 0

                while q:
                    r, c = q.popleft()
                    for d in range(4):
                        nx = r + dx[d]
                        ny = c + dy[d]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 :
                            # 육지라면 넘버링 계속 진행
                            if board[nx][ny] == 1:
                                q.append((nx, ny))
                                visited[nx][ny] = 1
                                board[nx][ny] = number  # 넘버링 진행
                                distance[nx][ny] = 0
                            
                            # 바다라면 (가장자리라는 말과 같음)
                            # 육지의 가장자리 좌표와 육지 번호 저장
                            elif board[nx][ny] == 0:
                                sea.append((r, c, number))

                number += 1



# 다리 놓기 
def extend(board):
    answer = float('inf')
    while sea :
        x,y,bridge = sea.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < n :
                # 바다라면 다리 설치
                if board[nx][ny] == 0 : 
                    board[nx][ny] = bridge
                    distance[nx][ny] = distance[x][y] + 1 
                    sea.append((nx,ny,bridge))
                
                # 섬과 섬이 이어졌을 떄 , 다른 다리와 만날 때
                elif board[nx][ny] != bridge:
                    answer = min(answer,distance[x][y]+distance[nx][ny])
    return answer 


    
numbering(board,1)
print(extend(board))

                number += 1



# 다리 놓기 
def extend(board):
    answer = float('inf')
    while sea :
        x,y,bridge = sea.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < n :
                # 바다라면 다리 설치
                if board[nx][ny] == 0 : 
                    board[nx][ny] = bridge
                    distanye[nx][ny] = distanye[x][y] + 1 
                    sea.append((nx,ny,bridge))
                
                # 섬과 섬이 이어졌을 떄 , 다른 다리와 만날 때
                elif board[nx][ny] != bridge:
                    answer = min(answer,distanye[x][y]+distanye[nx][ny])
    return answer 


    
numbering(board,1)
print(extend(board))
