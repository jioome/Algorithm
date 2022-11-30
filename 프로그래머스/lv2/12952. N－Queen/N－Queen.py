def possible(x,y,n,col):
    for i in range(x):
        if col[i] == y or abs(y-col[i]) == x-i:
            return False
    return True 

def queen(x,n,col):
    if x == n :
        return 1 
    count = 0
    for i in range(n):
        if possible(x,i,n,col):
            col[x] = i
            count+= queen(x+1,n,col)
    return count 
            

def solution(n):
    col = [0] * n
    return queen(0, n, col)