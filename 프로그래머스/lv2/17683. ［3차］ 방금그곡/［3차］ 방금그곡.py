def change(m):
    m = m.replace("C#","c").replace("D#","d").replace("E#","e").replace("F#","f").replace("G#","g").replace("A#","a").replace("B#","b")
    return m 

def solution(m, musicinfos):
    index = 0 
    answer = []
    m = change(m)
    for music in musicinfos : 
        index += 1 
        start,end,title, mu = music.split(',')
        hour = int(end[:2]) - int(start[:2])
        minute = int(end[-2:]) - int(start[-2:])
        play = 60*hour + minute
        print(play)
        changed = change(mu)
        a = len(changed)
        b = changed* (play // a) + changed[:play%a]
        if m in b : 
            answer.append([play,index,title])
    if not answer : 
        return "(None)"
    elif len(answer) == 1 : 
        return answer[0][2]
    else : 
        answer = sorted(answer, key=lambda x: (-x[0], x[1]))
        return answer[0][2] # 첫번째 제목을 리턴

