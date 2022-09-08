from collections import Counter    
from itertools import combinations
def solution(orders, course):
    answer = []
    
    for c in course :
        lst = [] 
        for o in orders : 
            lst+=list(map(''.join,(combinations(sorted(o),c))))
    
        lst = Counter(lst)
        print(lst)
        for a,b in lst.items() : 
            if b >=max(lst.values()) and b>=2 :
                print(a)
                answer.append(a)
            

    return sorted(answer)