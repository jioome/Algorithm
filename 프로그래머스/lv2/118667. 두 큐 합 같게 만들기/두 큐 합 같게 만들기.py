from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    t = len(q1)
    sum1 = sum(q1)
    sum2 = sum(q2)
    i = 0
    j = 0 
    while sum1 != sum2 and i < 2*t and j < 2*t : 
        if sum1 < sum2 : 
            num2 = q2.popleft() 
            sum1+= num2
            sum2-= num2 
            q1.append(num2)
            i+= 1
        else : 
            num1 = q1.popleft()
            sum1 -= num1
            sum2 += num1
            q2.append(num1)
            j+=1
    if sum1 == sum2 :
        answer = i+j
        return answer
        
        
    
    answer = -1
    
    return answer