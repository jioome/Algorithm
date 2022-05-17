import math
import sys


input = sys.stdin.readline

n,k,d  = map(int,input().split())
rule = []
for _ in range(k):
    a,b,c = map(int,input().split())
    rule.append((a,b,c))

def dotori(pivot):
    total = 0 
    for start,end, step in rule : 
        beta = min(end,pivot)
        if start <= beta :
            calc = (beta-start) // step + 1 # 넣을 수 있는 도토리의 수 
            total += calc # 총 도토리의 개수 구하기 
    return total 

lo,hi = 1,1000000 # 상자의 수 초기화 
ans = 0 
while lo <= hi : 
    mid = (lo+hi)//2
    if dotori(mid) >= d : 
        ans = mid 
        hi = mid - 1
    else : 
        lo = mid + 1 
print(ans)