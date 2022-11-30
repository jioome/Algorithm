def solution(arr):
    answer = 0

    num = 1 
    for i in range(len(arr)):
        a = arr[i]
        for i in range(min(num,a),0,-1):
            if a%i == 0 and num%i ==  0 : 
                num = a*num // i
                break
        
            

    return num