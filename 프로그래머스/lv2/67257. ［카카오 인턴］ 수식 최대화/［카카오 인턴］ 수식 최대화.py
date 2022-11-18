from itertools import permutations
def solution(expression):
    '''
    가장 큰 값 
    
    '''
    op = ["*","-","+"]
    op = list(permutations(op,3))
    result = [] 
    answer = 0
    def operation(n1,n2,op):
        num = 0 
        if op =='*':
            num = int(n1)* int(n2)
        elif op == '+':
            num = int(n1)+ int(n2)
        else : 
            num = int(n1)- int(n2)
        return num
    def calculate(exp,op):
        array=[]
        tmp=""
        for i in exp:
            if i.isdigit()==True:
                tmp+=i
            else:
                array.append(tmp)
                array.append(i)
                tmp=""
        array.append(tmp)

        for o in op:
            stack=[]
            while len(array)!=0:
                tmp=array.pop(0)
                if tmp==o:
                    stack.append(operation(stack.pop(), array.pop(0), o))
                else:
                    stack.append(tmp)
            array=stack

        return abs(int(array[0]))
        
    
    
    for i in op:
        result.append(calculate(expression, i))
    return max(result)