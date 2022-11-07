def solution(n, lost, reserve):
    answer = 0
    c = set(lost)&set(reserve)
    l = set(lost)-c
    r = set(reserve) - c
    
    for i in r : 
        if i-1 in l:
            l.remove(i-1)
        elif i+1 in l : 
            l.remove(i+1)
    answer = n - len(l)
    return answer