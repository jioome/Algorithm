def solution(number, k):
    answer = ''
    col = [] 
    
    for n in number : 
        while len(col) > 0 and col[-1] < n and k >0 : 
            
            col.pop()
            k -= 1 
        col.append(n)
    if k > 0 : 
        col = col[:-k]
    answer = ''.join(col)
            
    return answer