def dfs(numbers,target,depth):
    answer = 0 
    if depth == len(numbers):
        if target == sum(numbers):
            return 1
        else : 
            return 0 
    else : 
        answer += dfs(numbers,target,depth+1)
        numbers[depth] *= -1 
        answer += dfs(numbers,target,depth+1)

    return answer
        
def solution(numbers, target):
    
    answer = dfs(numbers,target,0)
    return answer
    
    
    

    
#     if depth == len(numbers):
#         if target ==sum(numbers):
#             return 1
        
#         else : 
#             return 0
#     else : 
#         answer += dfs(numbers,target,depth+1)
#         numbers[depth] *= -1
#         answer += dfs(numbers,target,depth+1)
#         return answer
# def solution(numbers, target):
#     answer = dfs(numbers,target,0)
#     return answer