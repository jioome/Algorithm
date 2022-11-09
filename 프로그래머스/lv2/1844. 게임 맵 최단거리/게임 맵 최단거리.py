from collections import deque
def solution(maps):
    '''
    bfs 방식 최소값 
    '''
    q = deque()
    q.append((1,1))
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    n = len(maps)
    m = len(maps[0])
    visited = [[0]*(m+1) for _ in range(n+1)]
    board = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            board[i+1][j+1] = maps[i][j]
    visited[1][1] = 1
    board[1][1] = 1 

    while q : 
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n+1 and 0 <= ny < m+1 and board[nx][ny] == 1 and visited[nx][ny] == 0 :
                visited[nx][ny] =1 
                board[nx][ny] = board[x][y]+1 

                q.append((nx,ny))
    
    
    answer = 0
    if board[n][m] == 1 :
        answer = -1
    else : 
        answer = board[n][m]
    
    return answer