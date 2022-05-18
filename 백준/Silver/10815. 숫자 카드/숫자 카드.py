import sys


input = sys.stdin.readline


n = int(input())
card = list(map(int, sys.stdin.readline().split()))
m = int(input())
check = list(map(int, sys.stdin.readline().split()))

card.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


for i in range(m):
    # check[i]가 card안에 있는지 확인 
    if binary_search(card, check[i], 0, n - 1) is not False: 
        print(1, end=' ')
    else:
        print(0, end=' ')