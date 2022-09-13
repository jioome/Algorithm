def check(answer):

    for x,y,kind in answer : 
        if kind == 0 : 
            if y != 0 and (x,y-1,0) not in answer and (x-1,y,1) not in answer and (x,y,1) not in answer : 
                return True 
        # 보일 때 
        else : 
            if (x,y-1,0) not in answer and  (x+1,y-1,0) not in answer and not ((x-1,y,1) in answer and (x+1,y,1) in answer) : 
                return True
    return False
        
        
    

def solution(n, build_frame):

    answer = set()

    for x,y,kind,status in build_frame : 
        idx = (x,y,kind)
        if status == 1 : 
            answer.add(idx)
            if check(answer) : 
                answer.remove((idx))
                
         # 삭제 
        elif (x,y,kind) in answer :
            answer.remove((x,y,kind))
            # 기둥
            if check(answer):
                print(1111)
                answer.add((x,y,kind))

    answer = list(answer)
    
    return sorted(answer, key = lambda x : (x[0],x[1],x[2]))
