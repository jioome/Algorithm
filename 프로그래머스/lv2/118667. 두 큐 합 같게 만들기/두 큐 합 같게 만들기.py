from collections import deque
def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    answer = -1
    s1 = sum(queue1)
    s2 = sum(queue2)
    if s1 == s2 : 
        return 0
    elif (s1+s2) % 2 == 1 : 
        return -1
    cnt = 0  
    for i in range(len(queue1)*3): 
        cnt += 1 
        if s1> s2:
            a = queue1.popleft()
            queue2.append(a)
            s1 -= a
            s2 += a
        else : 
            a = queue2.popleft()
            queue1.append(a)
            s2 -= a
            s1 += a

        if s1 == s2:
            return cnt
    
    
    return -1