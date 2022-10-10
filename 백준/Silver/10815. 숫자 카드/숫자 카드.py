import sys
sys.setrecursionlimit(10**9)
n = int(input())
card = list(map(int,input().split()))
card.sort()
m = int(input())
lst = list(map(int,input().split()))
answer = [] 



def binary_search(c): 
    left = 0 
    right = n-1
    while left <= right : 
        mid = (left+right)//2
        
        if card[mid] > c : 
            right = mid-1 
        elif card[mid] < c : 
            left = mid + 1
        else : 
            return 1
    return 0 

for c in lst : 
    answer.append(str(binary_search(c)))
print(' '.join(answer))