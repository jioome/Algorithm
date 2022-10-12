import heapq
import sys
input = sys.stdin.readline
InF = float('inf')


def dik_fox():
    dist = [InF]*(n+1)
    dist[1] = 0
    q = [] 
    heapq.heappush(q,(dist[1],1))

    while q : 
        d,c = heapq.heappop(q)
        if dist[c] < d : 
            continue
        for d1,c1 in g[c]:
            sd = d1 + d
            if dist[c1] > sd : 
                dist[c1] = sd 
                heapq.heappush(q,(sd,c1))
    return dist


def dik_wolf():
    # dist[0] 빠르게 도착 / dist[1] 느리게 도착
    dist = [[InF] * (n+1) for _ in range(2)]
    # 시작은 빠르게 달림 / 느린 거는 0 
    dist[1][1] = 0
    q = []
    heapq.heappush(q,(dist[1][1],1,False))

    # 빠르게 달릴 차례 -> false
    # 느리게 달릴 차례 -> True 
    while q:
        cd, ci, cf = heapq.heappop(q)
        if cf and dist[0][ci] < cd:
            continue
        elif not cf and dist[1][ci] < cd:
            continue

        for vd, vi in g[ci]:
            if cf:  # 빠르게 도착했다면, 느리게 출발
                nd = cd + (vd * 2)
                if nd < dist[1][vi]:
                    dist[1][vi] = nd
                    heapq.heappush(q, (dist[1][vi], vi, False))
            else:  # 느리게 도착했다면, 빠르게 출발
                nd = cd + (vd // 2)
                if nd < dist[0][vi]:
                    dist[0][vi] = nd
                    heapq.heappush(q, (dist[0][vi], vi, True))

    return dist


n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, d = map(int, input().split())
    # 계산을 정수로만 하기 위해 길이에 전부 2를 곱해줌
    g[a].append((d * 2, b))
    g[b].append((d * 2, a))

fox = dik_fox()
wolf = dik_wolf()

answer = 0
for i in range(1, n+1):
    if fox[i] < min(wolf[0][i], wolf[1][i]):
        answer += 1
print(answer)
