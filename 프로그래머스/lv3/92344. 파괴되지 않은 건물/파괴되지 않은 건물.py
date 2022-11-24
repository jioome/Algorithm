def solution(board, skill):
    '''
    [type, r1, c1, r2, c2, degree]
    1 공격
    2 회복
    '''
    answer = 0
    tmp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    # 누적합 구하는 방법으로 풀어야 시간초과가 안남 ,,, 알것냐
    for t, a,b,c,d,degree in skill : 
        if t == 2:
            degree = -degree
        tmp[a][b] -= degree
        tmp[a][d+1] += degree
        tmp[c+1][b] += degree
        tmp[c+1][d+1] -= degree
    for i in range(len(tmp)-1):
        for j in range(len(tmp[0])-1):
            tmp[i][j+1] += tmp[i][j]
    for i in range(len(tmp)-1):
        for j in range(len(tmp[0])-1):
            tmp[i+1][j] += tmp[i][j]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]+tmp[i][j] >0 : 
                answer += 1
    return answer
    
    