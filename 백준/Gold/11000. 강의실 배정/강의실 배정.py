import sys
import heapq

input = sys.stdin.readline 
n = int(input())
room = []
for _ in range(n):
    s,t = map(int,input().split())
    room.append([s,t])
room.sort()
heap = [] 
heapq.heappush(heap,room[0][1])
for i in range(1,len(room)) :
    if heap[0] <= room[i][0] : 
        heapq.heappop(heap)
        heapq.heappush(heap,room[i][1])
    else : 
        heapq.heappush(heap,room[i][1])

print(len(heap))
