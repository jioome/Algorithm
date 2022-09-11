def solution(msg):
    answer = []
    cnt = 27
    alpha = {}

    for i in range(1,27):
        alpha[chr(i+64)] = i 
    i = 0 
    s = ''
    
    while i< len(msg):
        s += msg[i]
        if s in alpha : 
            i+= 1 
        else : 
            alpha[s] = cnt
            cnt+=1 
            answer.append(alpha[s[:-1]])
            s ='' 
    
            
    # 마지막 거 넣기 
    answer.append(alpha[s])
        
    return answer