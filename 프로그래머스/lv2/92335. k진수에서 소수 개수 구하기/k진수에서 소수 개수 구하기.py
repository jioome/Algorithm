def change(n,k):
    p = []
    while n > k : 
        # 몫과 나머지를 구하는 함수 divmod
        n, mod = divmod(n,k)
        p.append(str(mod))
    p.append(str(n))
    p = p[::-1]
    p = ''.join(p)
    return p 

def isprime(n) :
    if n == 1 : 
        return False 
    if n == 2 :
        return True 
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0  : 
            return False
    return True 
            
    
        
def solution(n, k):
    num = change(n,k)
    num = num.split('0')
    cnt = 0
    for n in num : 
        if n and isprime(int(n)): 
            cnt += 1 
    return cnt
