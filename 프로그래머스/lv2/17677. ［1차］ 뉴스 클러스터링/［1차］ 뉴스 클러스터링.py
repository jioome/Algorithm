from itertools import combinations
from collections import Counter 
def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    a = [] 
    b = [] 
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            a.append(str1[i] + str1[i+1])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            b.append(str2[i] + str2[i+1])
            
    ca = Counter(a)
    cb = Counter(b)
    # 교집합 &
    inter = list((ca & cb).elements())
    # 합집합 |
    # elements() 카운터 숫자만큼 요소 반환 
    
    union = list((ca | cb).elements())
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)
    
