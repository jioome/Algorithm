import sys

input = sys.stdin.readline 
cnt = 0
 
while True : 
    answer = 0 
    cnt += 1 
    l,p,v = map(int,input().split())
    if l == 0 and p == 0 and v == 0 :
        break
    answer += (v // p) * l 
    if l < (v%p):
        answer += l
    else : 
        answer += v % p 

    print("Case {0}: {1}".format(cnt,answer))