from collections import Counter
def solution(participant, completion):
    answer = ''
    
    participant = Counter(participant)
    completion = Counter(completion)
    
    one = participant-completion
    for k,v in one.items():
        answer += k 
    
    return answer