from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    answer = -1
    cnt = 0
    sumq1 = sum(q1)
    sumq2 = sum(q2)
    len1 = len(q1)

    
    while cnt < len1*4 :
        if sumq1 < sumq2 : 
            a = q2.popleft()
            sumq1+= a 
            sumq2 -= a
            q1.append(a)
            cnt += 1
        elif sumq1 > sumq2 : 
            a = q1.popleft()
            sumq1 -= a
            sumq2 += a
            q2.append(a)
            cnt += 1 
        else : 
            
            return cnt
            
        
        
    
    
    return answer