from collections import defaultdict
def solution(id_list, report, k):
    report= set(report)
    answer = []
    user = defaultdict(list)
    receive = defaultdict(int)
    
    for r in report : 
        a,b = r.split(' ')
        user[a].append(b)
        receive[b] += 1

    result = []
    for id in id_list : 
        add = 0
        for j in user[id]:
            if receive[j] >=k : 
                add += 1 
        result.append(add)
                
    return result