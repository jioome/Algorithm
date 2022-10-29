def solution(rows, columns, queries):
    answer = []
    '''
    - 범위 찾기
    - 움직이는 것 중 가장 작은 것
    - 행 > 2 열 > 2 이래야 가운데 구멍이 생김 
    '''
    graph =[[0]*(columns+1) for _ in range(rows+1)]
    num = 1
    for i in range(1, rows+1):
        for j in range(1, columns+1): 
            graph[i][j] = num
            num += 1 
        
                     
    for x1,y1,x2,y2 in queries:
        tmp = graph[x1][y1]
        mini = tmp
        for k in range(x1,x2):
            test = graph[k+1][y1]
            graph[k][y1]= test
            mini = min(mini,test)
            
        for k in range(y1,y2):
            test = graph[x2][k+1]
            graph[x2][k]= test
            mini = min(mini,test)
        
        for k in range(x2,x1,-1):
            test = graph[k-1][y2]
            graph[k][y2] = test
            mini = min(mini,test)
        
        for k in range(y2,y1,-1):
            test = graph[x1][k-1]
            graph[x1][k] = test
            mini = min(mini,test)
        
        graph[x1][y1+1] = tmp
        answer.append(mini)
        
    
    return answer