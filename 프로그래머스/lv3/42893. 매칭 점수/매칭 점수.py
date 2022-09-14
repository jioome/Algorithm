import re 
from collections import defualtdict
def solution(word, pages):
    defualt_list = [] 
    outlink = [] 
    link_score = [] 
    matching = []
    word=word.lower()
    url_dict = {} 
    to_me_link = {}
    
    answer = 0
    for i in range(len(pages)) : 
    
        title = re.search('<meta property="og:url" content="(https://\S+)"', pages[i]).group(1)
        check_word = re.split('[^A-Za-z]',pages[i])
        lst = [] 
        # 기본 점수 
        for c in check_word:
            lst.append(c.lower())
        check_word = lst
        n = check_word.count(word)
        defualt_list.append(n)
        
        # 외부 링크 
        link_n = pages[i].count('</a>')
        outlink.append(link_n)
        
        # 링크 점수  
        for link in re.findall('<a href="(https://\S+)"', page):

            print(link)
        
        # web[i] = 
        self_num = defualt_list[i]/outlink[i]
    return answer
