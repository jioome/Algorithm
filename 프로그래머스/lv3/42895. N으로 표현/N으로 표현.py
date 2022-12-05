def solution(N, number):
    if N == number : 
        return 1
    s = [set() for _ in range(8)]

    # 2. 각 set마다 기본 수 "N" * i 수 초기화
    for x,a in enumerate(s,1):
        a.add(int(str(N)*x))

    answer = -1
    for i in range(1,8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 * op2)
                    s[i].add(op1 - op2)
                    if op2 != 0 : 
                        s[i].add(op1 // op2)
                    
    
        if  number in s[i] : 
            return i+1
    

    return answer