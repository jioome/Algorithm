import sys
input = sys.stdin.readline 
'''
투포인트를 쓰면 연속적인 거의 합을 구하기 좋을 거 같다 ,, 
근데 n이 겁나 크니까 머가 없을까 생각하면 투포인터를 생각하면 좋다 ,, 


구현 
'''

n,k = map(int,input().split())
day = list(map(int,input().split()))
s = 0 

for i in range(k):
    s += day[i]
max_s = s
for i in range(k,n):
    s = s -day[i-k] + day[i]
    max_s = max(max_s,s )

print(max_s)

