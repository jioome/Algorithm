def solution(enroll, referral, seller, amount):
    '''
    칫솔 한 개 판매해서 얻어지는 이익 
    dfs를 사용해서 타고 올라가면 딱일 거 같음 
    
    맨 위에는 민호가 있음 
    '''
    total = {} 
    answer = []
    graph = {}
    for i in range(len(enroll)):
        graph[enroll[i]]= graph.get(enroll[i],'')+ referral[i]
        total[enroll[i]] = 0 
    left = 0 
    def dfs(name,money) : 
        left = int(money*(0.1))
        total[name] += money - left
        
        if graph[name] == "-" or left == 0 :
            return 
        else : 
            dfs(graph[name],left)

        
    
    for i in range(len(seller)):
        dfs(seller[i],amount[i]*100)
    for e in enroll : 
        answer.append(total[e])

    return answer