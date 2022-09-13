from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    dict = {}
    total = defaultdict(int)
    for r in records : 
        t,n,s = r.split(' ')
        hour,minute = t.split(':')
        time = 60*int(hour) + int(minute)
        if n not in dict : 
            dict[n] = time
        else : 
            total[n] += time - dict[n]
            del dict[n]
    # out이 없는 경우 
    end = 23*60 + 59
    for d in dict : 
        total[d] += end-dict[d]
        
    
    print(total)
    ## 요금 구하기 ,, 
    default_time = fees[0]
    de_fare = fees[1]
    unit_time = fees[2]
    unit_fare = fees[3]
    
    # 차 번호 정렬 
    car_list = []
    for c in total : 
        car_list.append(c)
    car_list.sort()
    
    for c in car_list : 
        fare = 0
        time = total[c]
        if time >= default_time : 
            fare += de_fare
            time -= default_time
            fare += (math.ceil(time/unit_time)) * unit_fare
        else : 
            fare = de_fare
        answer.append(fare)
        
        
    
    
        

        
        
    
            
        
        
        

        
        
    return answer