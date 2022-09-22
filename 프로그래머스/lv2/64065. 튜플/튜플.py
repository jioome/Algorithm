def solution(s):
    answer = []
    lst = []
    s = s[1:-1]
    st = ''
    
    s = s.split('},{')
    for i in s : 
        i = i.replace('{','')
        i= i.replace('}','')
        lst.append(i)
    
    lst.sort(key = len)
    for l in lst : 
        a = l.split(",")
        for i in a : 
            if int(i) not in answer : 
                answer.append(int(i))
    print(answer)
    
        

    return answer 
    