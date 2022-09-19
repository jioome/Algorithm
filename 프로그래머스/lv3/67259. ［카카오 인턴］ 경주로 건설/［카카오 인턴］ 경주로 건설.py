from collections import deque
            

def solution(board):
    def bfs(start):
        answer = float('inf')
        n = len(board)
        q = deque()
        q.append(start)
        visited = [[float('inf')] * n for _ in range(n)] 
        visited[0][0] = 0 
        dir = {0:[-1,0],1:[0,1],2:[1,0],3:[0,-1]}
        

        
        while q : 
            x,y,c,d = q.popleft()
            for i in range(4): 
                
                nx =  x + dir[i][0]
                ny =  y + dir[i][1]
                if 0 <=nx <n and 0<= ny < n and board[nx][ny] != 1 :
                    rate  = c + 100 if d == i else c + 600
                    if visited[nx][ny] > rate  : 
                        visited[nx][ny] = rate
                        q.append((nx,ny,rate,i))
        
        return visited[-1][-1]
                        
                        
        
    
        
    
    return min([bfs((0, 0, 0, 1)), bfs((0, 0, 0, 2))]) # 오,아래