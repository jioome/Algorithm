from collections import deque
n,m = map(int,input().split())
fridge = [list(map(int,input().split())) for _ in range(n)]
cnt = 0


def bfs(a,b):
    # 매번 q, visited 초기화 
    q = deque()
    visited = [[0]*m for _ in range(n)]
    q.append((a,b))
    dx = [1,-1,0,0] 
    dy = [0,0,1,-1] 
    remove_cheese = 0 
    
    while q  :
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                # 공기
                if fridge[nx][ny] == 0 and visited[nx][ny] == 0: 
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                if  fridge[nx][ny]> 0 :
                    fridge[nx][ny] += 1 

    # 3 이상이면 녹아버리는 경우임  
    for i in range(n):
        for j in range(m):
            if fridge[i][j]>= 3 : 
                fridge[i][j] = 0 
                remove_cheese += 1
            elif fridge[i][j] == 2: 
                fridge[i][j] = 1 

    if remove_cheese > 0:
        return True
    else : 
        return False





while bfs(0,0) :
    cnt += 1  
    
print(cnt)