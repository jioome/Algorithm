def solution(record):
    answer = []
    msg = {"Enter":"님이 들어왔습니다.", "Leave":"님이 나갔습니다."}
    name = {}
    for r in record : 
        r = r.split(' ')
        if r[0] =="Enter" or r[0] == "Change":
            name[r[1]] = r[2]
    
    for r in record : 
        r = r.split(' ')
        if r[0] == 'Enter':
            answer.append(name[r[1]]+msg[r[0]])
        if r[0] == 'Leave':
            answer.append(name[r[1]]+msg[r[0]])

            
            
    return answer