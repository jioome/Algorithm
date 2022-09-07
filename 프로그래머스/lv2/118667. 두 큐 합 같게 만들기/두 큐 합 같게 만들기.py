from collections import deque
def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    for _ in range(len(queue1) * 3) :
        if sum1 < sum2 : 
            num2 = q2[0]
            sum2 -= num2
            sum1 += num2
            q1.append(q2.popleft())

        elif sum1 > sum2 : 
            num1 = q1[0]
            sum1 -= num1
            sum2 += num1
            q2.append(q1.popleft())

        else : 
            return answer
        answer += 1 
    return -1