from itertools import combinations_with_replacement as cwr
def solution(n, info):
    answer = [-1]
    maxgap = -1
    for com in cwr(range(11),n):
        info2= [0]*11
        # 이긴 횟수 
        lion,apeach = 0,0
        
        for i in com : 
            info2[10-i]+=1
            
        for i in range(11):
            if info[i] == info2[i] == 0 : 
                continue
            elif info[i] >= info2[i] : # 어피치가 이김 
                apeach += 10-i 
            else : 
                lion += 10-i
        if lion > apeach :
            gap = lion-apeach
            if maxgap < gap :
                maxgap = gap
                answer = info2

        
    return answer