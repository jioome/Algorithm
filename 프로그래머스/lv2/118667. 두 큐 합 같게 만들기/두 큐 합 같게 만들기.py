from collections import deque
def solution(queue1, queue2):
    answer = 0
    # 시간 초과 방지 
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    # *3을 해야하는 이유 
    # L1 -> a + 2
    # R1 -> n + a  a는 최대 n-1
    for _ in range(len(queue2) * 3) :
        if sum1 < sum2 : 
            num2 = q2.popleft()
            sum2 -= num2
            sum1 += num2
            q1.append(num2)

        elif sum1 > sum2 : 
            num1 = q1[0]
            sum1 -= num1
            sum2 += num1
            q2.append(q1.popleft())

        else : 
            return answer
        answer += 1 
    return -1