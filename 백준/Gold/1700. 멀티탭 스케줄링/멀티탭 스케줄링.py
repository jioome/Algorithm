import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))
plugin = []
answer = 0
for i in range(k):
    if arr[i] in plugin:
        continue
    if len(plugin) < n:
        plugin.append(arr[i])
        continue
     
    # 플러그를 뽑아야 함
    answer += 1
    out = 0  # 뽑을 플러그
    outidx = 0  # out이 이후 몇 번째에 사용되는지 (arr에서 인덱스)
    for j in range(n):
        try:
            idx = arr[i+1:].index(plugin[j])
            if idx > outidx:
                out = j
                outidx = idx
        except: 
        # 이후 사용되지 않는 플러그가 있다면 걔를 뽑으면 된다.
            out = j
            break
    plugin[out] = arr[i]
print(answer)


