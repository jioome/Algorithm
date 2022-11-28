def solution(n, k, cmd):
    '''
    linked 리스트로 푸는 문제였다네  
    
    '''
    answer = ''
    linked_list = {i:[i-1,i+1] for i in range(n)}
    table = ['O']*n
    delete = [] 
    for c in cmd :
        c = c.split(' ')
        if c[0] == 'D':
            for _ in range(int(c[1])):
                k = linked_list[k][1]
        elif c[0] == 'U':
            for _ in range(int(c[1])):
                k = linked_list[k][0]
        # 삭제 하는 법 
        elif c[0] == 'C':
            prev,nxt = linked_list[k]
            table[k] = 'X'
            delete.append((prev,k,nxt))
            
            # 삭제하고 나서 k 값
            if nxt == n : 
                k = prev
            else : 
                k = nxt
            
            if prev == -1 : 
                linked_list[nxt][0] = prev
            elif nxt == n : 
                linked_list[prev][1] = nxt
            else : 
                linked_list[prev][1] = nxt
                linked_list[nxt][0] = prev
                
        # 가장 최근에 삭제된 행을 원래대로 복구
        else : 
            prev,now,nxt = delete.pop()
            table[now] = 'O'
            
            if prev == -1 : 
                 linked_list[nxt][0] = now
            elif nxt == n : 
                linked_list[prev][1] = now
            else : 
                linked_list[prev][1] = now
                linked_list[nxt][0] = now
            
        
                

    return ''.join(table)