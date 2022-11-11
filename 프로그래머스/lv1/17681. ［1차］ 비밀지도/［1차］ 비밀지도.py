
def solution(n, arr1, arr2):
    '''
    공백, 벽 
     
    '''
    answer = []
    board = ['' for _ in range(n)]
    board2 = ['' for _ in range(n)]
    for i in range(len(arr1)) : 
        numbi =bin(arr1[i])[2:]
        if len(numbi) < n : 
            board[i]+='0'*(n-len(numbi)) + numbi
        else : 
            board[i] += numbi
    for i in range(len(arr2)) : 
        numbi =bin(arr2[i])[2:]
        if len(numbi) < n : 
            board2[i]+='0'*(n-len(numbi)) + numbi
        else : 
            board2[i]+= numbi
    new = ['' for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == "1" or board2[i][j] == "1":
                new[i]+= "1"
            else : 
                new[i]+= "0"
            
            

    for b in new : 
        b =b.replace("1","#")
        b = b.replace("0"," ")
        answer.append(b)        

    return answer
            