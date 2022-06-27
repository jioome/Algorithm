n, b = map(int, input().split())
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = ''
while n:
    s += str(arr[n % b])
    n //= b

print(s[::-1])