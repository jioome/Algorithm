def solution(m, n, board):
    ans, board = 0, [list(b) for b in board]
    while True:
        popped = False
        temp = set()
        # 순차 탐색하며 지워지는 블록들의 인덱스 저장
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != 0 and \
                board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                    temp.add((i, j))
                    temp.add( (i + 1, j))
                    temp.add((i, j + 1))
                    temp.add((i + 1, j + 1))
                    popped = True
                    
        # 지워진 블록이 없다면 반복문 탈출            
        if popped == False:
            break
		
        # 지워지는 블록 0으로 처리하면서 정답 갱신
        for i, j in list(temp):
            board[i][j] = 0
            ans += 1
        
        for i in range(m)[::-1]:
            for j in range(n):
                if board[i][j] == 0:
                    x = i-1
                    while x>=0 and board[x][j] == 0 : 
                        x-= 1 
                    if x>= 0 : 
                        board[i][j],board[x][j] = board[x][j],0

                    

    return ans