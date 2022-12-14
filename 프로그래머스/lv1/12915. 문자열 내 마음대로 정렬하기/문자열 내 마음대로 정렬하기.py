def solution(strings, n):
    answer = []
    strings.sort()
    arr = [] 
    for i in range(len(strings)):
        word = strings[i]
        arr.append((word[n],i))
    arr.sort()
    for w,idx in arr : 
        answer.append(strings[idx])
        
    return answer