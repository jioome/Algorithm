import re 
from collections import defaultdict
def solution(word, pages):
    default_list = {}
    outlink = {}

    matching = []
    word=word.lower()
    url_dict = {} 
    to_me_link = defaultdict(list)

    answer = 0
    cnt = 0 

    for i in range(len(pages)) : 

        title = re.search('<meta property="og:url" content="(https://\S+)"', pages[i]).group(1)

        check_word = re.split('[^A-Za-z]',pages[i])
        lst = [] 
        # 기본 점수 
        for c in check_word:
            lst.append(c.lower())
        check_word = lst
        n = check_word.count(word)
        default_list[title]=n

        # 외부 링크 
        link_n = pages[i].count('</a>')
        outlink[title] = link_n

        # 링크 점수  
        for link in re.findall('<a href="(https://\S+)"', pages[i]):
            to_me_link[link].append(title)

    for curr in default_list : 
        score = 0
        score += default_list[curr]
        for to in to_me_link[curr] : 
            score += default_list[to]/outlink[to]
        matching.append(score)
    answer = matching.index(max(matching))
    return answer