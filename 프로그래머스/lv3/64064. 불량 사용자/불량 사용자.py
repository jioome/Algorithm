from itertools import permutations
import re 
def solution(user_id, banned_id):
    answer = 0
    # 조인할 때 문자열 구분해주기 위한 것 
    ban = '/'.join(banned_id).replace("*",'.')
    answer = set()
    for i in permutations(user_id,len(banned_id)):
        if re.fullmatch(ban,'/'.join(i)):
            answer.add(''.join(sorted(i)))

        
    
    return len(answer)