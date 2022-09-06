import re
def solution(new_id):
    answer = ''
    #1 
    new_id = new_id.lower()
    #2 정규표현식
    new_id = re.sub('[^0-9a-z-_.]','',new_id)
    #3 
    new_id = re.sub('\.+','.',new_id)
    #4
    if new_id.startswith('.'):
        new_id = new_id[1:]
    if new_id.endswith('.'):
        new_id = new_id[:-1]
    # 5
    if len(new_id) == 0 : 
        new_id = "a"
    #6
    if len(new_id) >=16:
        new_id = new_id[:15]
    if new_id.endswith('.'):
        new_id = new_id[:-1]
    
    #7
    while len(new_id) <= 2:
        new_id += new_id[-1]


    return new_id