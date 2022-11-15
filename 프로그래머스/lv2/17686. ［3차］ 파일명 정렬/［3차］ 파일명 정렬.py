def solution(files):
    '''
    3가지 
    '''
    answer = []
    
    num = []
    for f in files :
        digit = ''
        head = ''
        tail = ''
        real_head = ''
        check = False
        for i in range(len(f)): 
            if not check and not f[i].isdigit():
                real_head += f[i] 
                head+= f[i].lower()
            if f[i].isdigit():
                check = True 
                digit += f[i] 
            if check and not f[i].isdigit():
                tail+=f[i:]
                break
        
        num.append((real_head+str(digit)+tail, head, int(digit) ))

    num.sort(key =lambda x : (x[1],x[2]))

    for a,b,c in num : 
        answer.append(a)
        
        
                
        
    return answer