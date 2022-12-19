def solution(n, times):
    answer = 0
    start = 0
    end = max(times) * n
    
    while start <= end :
        num = 0 
        time = (start+end) // 2
        for i in times :
            num+= (time//i)
        if num >= n : 
            end = time -1 
        elif num < n : 
            start = time + 1 
            
    answer = start
    return answer