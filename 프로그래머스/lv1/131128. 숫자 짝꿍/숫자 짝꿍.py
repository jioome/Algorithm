from collections import Counter
def solution(X, Y):
    answer = ''
    countx = Counter(X)
    county = Counter(Y)
    countz = countx&county
    
    clist = sorted(countz.items(),reverse=True)
    print(clist)
    if not clist:
        return "-1"
    if clist[0][0] == "0":
        return "0"
    for k in clist:
        answer+=k[0]*int(k[1])
    return answer
    