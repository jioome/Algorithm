def solution(n):
    answer = 0
    for i in range(1,n+1):
        cnt = i 
        while cnt < n : 
            i += 1
            cnt += i
        if cnt == n : 
            answer += 1 
            
    return answer