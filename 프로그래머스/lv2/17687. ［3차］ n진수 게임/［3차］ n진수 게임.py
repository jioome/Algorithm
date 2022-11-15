def solution(n, t, m, p):
    
    answer = ''
    num = m*t 
    result= '0'
    
    
    
    for i in range(1, m*t): 
        lst = ''
        while i : 
            mod = i % n 
            i = i // n 
            if 10 <= mod <=15: 
                mod = hex(mod)[2:].upper()
            lst +=str(mod)
    
        lst =lst[::-1]
        result += lst
    idx = p-1

    for i in range(t):
        answer+= result[idx]
        idx += m

    
    return answer