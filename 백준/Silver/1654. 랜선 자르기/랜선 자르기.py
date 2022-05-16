import sys

input = sys.stdin.readline 
k,n = map(int, input().split())

line =[] 
for _ in range(k):
    line.append(int(input()))

start = 1
end = max(line)

while start <= end : 
    cnt = 0 
    mid = (start+end)//2 
    for l in line : 
        cnt += (l//mid)

    if cnt >= n : 
        start = mid + 1 
    else : 
        end = mid -1

print(end)
