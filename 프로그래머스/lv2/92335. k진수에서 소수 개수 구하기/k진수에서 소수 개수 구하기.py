def isprime(x) : 
    for i in range(2,int(x**0.5)+1) : 
        if int(x)% i == 0 : 
            return False
    return True
    
    
def solution(n, k):
    count = 0 
    div = n//k
    result = []
    while div > 0:
        result.append(n % k)
        n = div
        div = n//k
    result.append(n % k)
    result.reverse()
    prime = []
    p = ''
    for r in result : 
        if r == 0 : 
            if len(p) > 0 and p!= '1': 
                prime.append(p)
                p = '' 
            if p == '1' : 
                p = ''
            
        else : 
            p+= str(r)
            
    if len(p) > 0 and p!= '1': 
                prime.append(p)
    
    for pr in prime : 
        if isprime(int(pr)): 
            count += 1 


    return count