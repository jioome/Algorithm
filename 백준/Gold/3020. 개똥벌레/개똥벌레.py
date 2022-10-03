import sys 
input = sys.stdin.readline 
n,h = map(int,input().split())


# 누적합 
lines = [0]*h

for i in range(n):
    high = int(input())

    # 종유석
    if i% 2 == 0 : 
        lines[h-high] += 1 
    # 석순
    else : 
        lines[0] += 1
        lines[high] -= 1

for i in range(1,h):
    lines[i] += lines[i-1]

count = 0 
low = min(lines)
for i in lines : 
    if i == low : 
        count += 1
print(low,count)