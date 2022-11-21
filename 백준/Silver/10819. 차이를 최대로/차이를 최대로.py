import sys
from itertools import permutations
 # 순열로 푸는게 훨씬 쉬움 

def back_tracking():
    global answer
    # stack 길이 n되면 최댓값 갱신
    if len(stack) == n : 
        sum_ = 0 
        for idx in range(1,n):
            sum_ += abs(a[stack[idx-1]]-a[stack[idx]])
        if answer < sum_:
            answer = sum_
        return 
    else : 
        for index in range(n):
            if index not in stack : 
                stack.append(index)
                back_tracking()
                stack.pop()
                # 재귀함수 return되면 pop

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
global answer
answer = 0
stack =[] 
back_tracking()
print(answer)

