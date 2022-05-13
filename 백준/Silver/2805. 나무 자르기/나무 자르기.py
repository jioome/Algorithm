import sys


n,m = map(int,input().split())
tree = list(map(int,input().split()))

first,last = 1, max(tree)
while first <= last:
    mid = (first+last)//2
    answer = 0 # 절단 했을 때 가져가는 나무 높이 합 
    for t in tree :
        if (t-mid) > 0 :
            answer += (t-mid)
    if answer >= m : 
        first = mid + 1 
    else : 
        last = mid -1 
print(last)