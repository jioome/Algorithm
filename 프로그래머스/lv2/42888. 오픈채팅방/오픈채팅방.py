def solution(record):
    answer = []
    name = {}
    for r in record : 
        r = r.split(' ')
        if r[0] == 'Change' or r[0] == 'Enter' : 
            name[r[1]] = r[2]
            
    for r in record : 
        r = r.split(' ')
        if r[0] == 'Enter':
            a = name[r[1]]
            answer.append(a+"님이 들어왔습니다.") 
        if r[0] == 'Leave':
            a = name[r[1]]
            answer.append(a+"님이 나갔습니다.") 
            
    return answer