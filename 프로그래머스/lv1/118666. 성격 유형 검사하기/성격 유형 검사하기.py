from collections import Counter
def solution(survey, choices):


    c1 = {"R":0,"T":0} 
    c2 = {"C":0,"F":0} 
    c3 = {"J":0,"M":0} 
    c4 = {"A":0,"N":0} 
    answer = ''
    
    for i in range(len(survey)):
        score = choices[i]
        f = 0 
        if score < 4 : 
            score = 4-score
            f = 1
        else : 
            score = choices[i]%4

        if survey[i][0] in c1 :
            if f == 1 : 
                c1[survey[i][0]] += score
                print(score)

            else : 
                c1[survey[i][1]] += score
                print(score)
        elif survey[i][0] in c2 :
            if f == 1 : 
                c2[survey[i][0]] += score
                print(score)
            
            else : 
                c2[survey[i][1]] += score
        elif survey[i][0] in c3 :
            if f == 1 : 
                c3[survey[i][0]] += score
            
            else : 
                c3[survey[i][1]] += score
        elif survey[i][0] in c4 :
            if f == 1 : 
                c4[survey[i][0]] += score
            
            else : 
                c4[survey[i][1]] += score
    
    for k,i in Counter(c1).most_common(1):
        if i != 0 : 
            answer += k 
        else : 
            answer += sorted(c1.keys())[0]
    for k,i in Counter(c2).most_common(1):
        if i != 0 : 
            answer += k 
        else : 
            answer += sorted(c2.keys())[0]
    for k,i in Counter(c3).most_common(1):
        if i != 0 : 
            answer += k 
        else : 
            answer += sorted(c3.keys())[0]
    for k,i in Counter(c4).most_common(1):
        if i != 0 : 
            answer += k 
        else : 
            answer += sorted(c4.keys())[0]
    return answer