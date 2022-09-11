from itertools import combinations
def solution(relation):
    answer = 0
    col = len(relation[0])
    row = len(relation)
    combi = [] 
    # 후보키 가능 경우의 수 
    for i in range(1,col+1):
        combi+= combinations(range(col),i)

    # 유일성
    unique = [] 
    
    for com in combi :
        only = [] 
        for r in relation : 
            only+= [r[c] for c in com ]
        if len(set(only)) == row : 
            check = True 
            for x in unique :
                # 최소성 확인 
                if set(x).issubset(set(com)):
                    check = False
                    break
            if check : 
                unique.append(com)
        
        
        
    return len(unique)
