import sys

n = int(input())
k = int(input())

sensor = list(map(int,input().split()))

sensor.sort() # 인접한 센서 사이 거리 구하기 위해 
between = []
for i in range(1,len(sensor)):
    between.append(sensor[i]-sensor[i-1]) # 인접한 센서 사이의 거리 
between.sort()
answer = sum(between[:n-k]) # k개의 집중국 필요하면 k-1개 사이가 필요

print(answer)