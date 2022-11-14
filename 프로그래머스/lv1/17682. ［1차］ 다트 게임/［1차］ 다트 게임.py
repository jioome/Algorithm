def solution(dartResult):
    '''
    *스타상 첫번째도
    
    '''
    pre = ''
    answer = []
    for d in dartResult:
        if pre.isdigit() and d.isdigit():
            answer.pop()
            answer.append(int(pre+d))
        elif d.isdigit():
            answer.append(int(d))
        
                
        elif d.isalpha():
            if d == "S":
                answer[-1] = answer[-1]**1
            if d == "D":
                answer[-1] = answer[-1]**2
            if d == "T":
                answer[-1] = answer[-1]**3
        else : 
            if d == "*":
                answer[-1] *= 2
                if len(answer) >1:
                    answer[-2] *= 2
            if d == '#':
                answer[-1] *= -1
        pre = d
    answer = sum(answer)
    return answer