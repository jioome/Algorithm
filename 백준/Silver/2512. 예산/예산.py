import sys

n = int(input())
request = list(map(int,input().split()))
money = int(input())
answer = 0 # 상한액
start = 0 
end = max(request) 

while start <= end : 
    mid = (start+end) // 2
    answer = 0  
    for r in request : 
        if r >= mid : 
            answer += mid
        else : 
            answer += r 
    if answer <= money :  
        start = mid +1 
    else : 
        end = mid -1 

print(end)
