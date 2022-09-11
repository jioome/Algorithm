from itertools import combinations

def solution(relations):
    row, col = len(relations), len(relations[0])
    candidates = []

    for i in range(1, col + 1):
        candidates.extend(combinations(range(col), i))

    unique = []
    for candidate in candidates:
        temp = [tuple([relation[i] for i in candidate]) for relation in relations]

        # 유일성 보장 
        if len(set(temp)) == row:
            check = True
            
            for u in unique:
                # u 가 candidate에 속해 있는지 
                if set(u).issubset(set(candidate)):
                    check = False
                    break
            
            if check:
                unique.append(candidate)

    return len(unique)