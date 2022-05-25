def divided(p):
    cnt = 0
    for i in range(len(p)) : 
        if p[i] =='(' : 
            cnt += 1 
        else :
            cnt -= 1 
        if cnt == 0 :
            u = p[:i+1]
            v = p [i+1 : ]
            return u,v
    
# 올바른 문자열인지 확인 
def check_balance(u) : 
    cnt = 0
    for i in u :  
        if i =='(' : 
            cnt += 1 
        else : 
            cnt -=1 

        if cnt < 0 :
            return False
    return True
#     stack = []

#     for p in u:
#         if p == '(':
#             stack.append(p)
#         else:
#             if not stack:
#                 return False
#             stack.pop()

#     return True

def solution(p):
    if not p :
        return ''
    u, v = divided(p)
    
    if check_balance(u) : 
        return u + solution(v)
    else : 
# 올바른 문자열로 만들기 
        # 과정 4-1
        answer = '('
        # 과정 4-2
        answer += solution(v)
        # 과정 4-3
        answer += ')'

        # 과정 4-4
        for p in u[1:len(u) - 1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('
            
            
    return answer