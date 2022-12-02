def solution(s):
    answer = ''
    prev = ' '
    for i in s:
        i=i.lower()
        if prev == ' ' and i.isalpha():
            i=i.upper()
            
        answer += i
        prev = i    
        
    return answer