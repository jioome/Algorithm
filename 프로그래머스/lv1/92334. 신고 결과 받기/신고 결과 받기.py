from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    report= set(report)
    cnt = defaultdict(int)
    mail = defaultdict(list)
    stop = [] 

    for r in report : 
        a,b = r.split(' ')
        cnt[b] += 1
        mail[a].append(b)
        

    for c in cnt.items():
        if c[1]>=k : 
            stop.append(c[0])

    if not stop : 
        return [0]*len(id_list) 
    

    for i in id_list : 
        cnt = 0 
        for m in mail[i]:
            if m in stop : 
                cnt += 1 
        answer.append(cnt)
        
        
        
    return answer