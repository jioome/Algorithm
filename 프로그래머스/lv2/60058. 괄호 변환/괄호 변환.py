def right(u) : 
    r = 0
    for j in u : 
        if j == ')':
            r -= 1
        else : 
            r += 1 
        if r < 0 : 
            return False
    return True
        

def solution(p):
    answer = ''
    # 1 
    if len(p) == 0: 
        return ''

    # 2 
    cnt = 0
    u = ''
    v = ''
    # 균형
    for i in range(len(p)) :
        if p[i] =='(' : 
            cnt += 1 
            u += p[i]
        else : 
            cnt -= 1
            u += p[i]
        if cnt == 0 :
            v = p[i+1:]
            break
    # 이 부분이 헷갈림 ,, 
    if right(u) : 
        return u + solution(v)
    else : 
        answer += '('
        answer += solution(v)
        answer += ')'
        u = u[1:-1]
        for j in u : 
            if j == '(':
                answer += ')'
            else : 
                answer += '('
    
                

    return answer