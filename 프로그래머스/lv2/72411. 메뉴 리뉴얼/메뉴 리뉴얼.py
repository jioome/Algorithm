from collections import Counter    
from itertools import combinations
def solution(orders, course):
    answer = []
    
    for c in course :
        lst = [] 
        for o in orders : 
            # map 이용 / xy , yx 조합 같게 만들기 위해 sorted 
            lst+=list(map(''.join,(combinations(sorted(o),c))))
        lst = Counter(lst)
        for a,b in lst.items() : 
            if b >=max(lst.values()) and b>=2 :
                answer.append(a)
            

    return sorted(answer)
