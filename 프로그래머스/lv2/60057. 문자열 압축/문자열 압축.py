def solution(s):
    result = []
    if len(s) == 1 : 
        return 1
    for i in range(1,len(s)//2+1): # i자씩 끊기 
        cnt = 1
        b = ''
        tmp  = s[:i]
        for j in range(i,len(s)+i,i) :

            if tmp == s[j: j+i] : 
                cnt += 1
            else : 
                if cnt !=1 : 
                    b += str(cnt) + tmp
                else : 
                    b += tmp 
                    
                cnt = 1
                tmp = s[j: j+i]

        
        result.append(len(b))

            
            

    
    return min(result)