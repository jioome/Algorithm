from itertools import combinations
from collections import Counter
def solution(orders, course):
    sorted(orders)
    result = [] 
    for c in course : 
        p = [] 
        for order in orders : 
            p+=list(map(''.join,combinations(sorted(order),c)))
        cntp = Counter(p)
        for k in cntp:
            if cntp[k] >= 2 and cntp[k] == max(cntp.values()) : 
                result.append(k)

    return sorted(result)