import sys

input = sys.stdin.readline 
n, l = map(int,input().split())
sinks = list(map(int,input().split()))
sinks.sort()
tape = 0 
cnt = 0

for sink in sinks : 
    if tape < sink : 
        tape = sink + l -1 # 0.5의 여유 공간이 있어야 하므로 -1 을 빼준다. 
        cnt += 1 
    else : 
        continue

print(cnt)




    
