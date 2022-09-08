from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    report = set(report)
    bad = defaultdict(int)
    rman = defaultdict(list)
    badlst = [] 
    for r in report : 
        a,b = r.split(' ')
        bad[b] += 1 
        rman[a] += [b]
    
    for b,n in bad.items() : 
        if n>=k : 
            badlst.append(b)
    if len(badlst) == 0 :
        answer = [0]*len(id_list)
        return answer 


    for i in id_list : 
        cnt= 0 
        for a in rman[i]:
            if a in badlst : 
                cnt +=1 
        answer.append(cnt)
            
    return answer