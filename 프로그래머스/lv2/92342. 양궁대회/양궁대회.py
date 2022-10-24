from itertools import combinations_with_replacement as cwr

def solution(n, info):
    answer = [-1]
    maxgap = -1
    
    for combi in cwr(range(11),n):
        # 라이언
        info2 = [0]*11
        apeach, lion = 0,0
        
        for i in combi:
            info2[10-i] += 1
        
        for idx in range(11):
            if info[idx] == info2[idx] == 0 : 
                continue
            elif info[idx]>=info2[idx]: # 어피치가 점수 높음
                apeach += 10-idx
            else :  # 라이언이 점수 높음 
                lion += 10 - idx
                
        if lion > apeach : # 라이언이 이김 
            gap = lion- apeach
            if gap > maxgap:
                maxgap = gap
                answer = info2
                
    return answer