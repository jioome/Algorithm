from collections import defaultdict
from itertools import combinations
from bisect import bisect_left
def solution(info, query):
    answer = []
    dict = defaultdict(list)
    info_dict = defaultdict(list)
    
    
    for i in info : 
        i = i.split(' ')
        s = int(i[-1])
        i = i[:-1]
        for j in range(5):
            for c in combinations(i,j):
                tmp = ''.join(c)
                info_dict[tmp].append(s)
    
    for i in info_dict : 
        info_dict[i].sort()
    
# 쿼리 분리 
    for q in query :
        q = q.split(' ')
        score = int(q[-1])
        q =q[:-1]
        q = ''.join(q)
        q=q.replace('-','')
        q=q.replace('and','')
        cnt = 0 
        for i in info_dict : 
            if i == q : 
                target = info_dict[i]
                idx = bisect_left(target,score)
                cnt = len(target)-idx
            
        answer.append(cnt)
        
    return answer