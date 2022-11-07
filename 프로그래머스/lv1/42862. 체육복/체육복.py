def solution(n, lost, reserve):
    answer = 0
    u = [1] *(n+2)
    for i in reserve : 
        u[i] += 1 
    for l in lost : 
        u[l] -= 1
    for i in range(1,n+1):
        if u[i-1] == 0 and u[i] == 2 : 
            u[i-1] = 1 
            u[i] = 1
        elif u[i+1] == 0 and u[i] == 2 : 
            u[i+1] = 1 
            u[i] = 1
    print(u)
    lst = [x for x in u[1:-1] if x >0]
    
    return len(lst)