from itertools import * 
n = int(input())
board = [list(map(int,input().split()))for _ in range(n)]
member= list(range(n))
result = float('inf')

# 능력차 최소가 되게 하기 

coms = list(combinations(range(n),n//2))
for com in coms : 
    member= list(range(n))
    sum1 = 0 
    sum2 = 0 
    # 스타트팀
    for a,b in combinations(com,2):
        sum1 += board[a][b] + board[b][a]
    # 링크팀 구하기 
    for c in com:
        member.remove(c)
        
    for a,b in combinations(member,2):
        sum2 += board[a][b] + board[b][a]
    
    result = min(result,abs(sum1-sum2))
    
print(result)   


    
