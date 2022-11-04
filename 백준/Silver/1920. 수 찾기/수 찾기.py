import sys
input = sys.stdin.readline 
'''
있는지 없는지 찾는 거 ,, 
이분탐색이 매우 빠름 ,, 
수가 엄청 큼 
이분 탐색을 정렬되어 있을 때만 쓸 수 있음 ,,, 
'''
n = int(input())
a = list(map(int,input().split()))
m = int(input())
num = list(map(int,input().split()))

a.sort()
for target in num : 
    start = 0 
    end = n -1
    check = 0 
    while start <= end : 
        mid = (start+end) // 2
        if a[mid] < target : 
            start = mid + 1 
        elif a[mid] > target : 
            end = mid - 1
        else : 
            check = 1
            break 
    if check == 1 : 
        print(1)
    else : 
        print(0)