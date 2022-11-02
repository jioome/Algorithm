dx = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dy = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]
directions = [1,2,3,4,5,6,7,8,9]
R, C = map(int, input().split())
arr = [[0] * C for _ in range(R)]
x, y = 0, 0
aduinosDict = {}
aduinos = []
for i in range(R):
    li = input()
    for j in range(C):
        arr[i][j] = '.'
        if li[j] == "I":
            x, y = i, j
        elif li[j] == "R":
            aduinosDict[(i,j)] = 1
            aduinos.append((i,j))
            continue
        aduinosDict[(i,j)] = 0


cmd = input()
cnt = 1
fin = False
while True:
    if cnt > len(cmd):
        fin=True
        break
    nowDir = int(cmd[cnt-1])
    x = x + dx[nowDir]
    y = y + dy[nowDir]

    if aduinosDict[(x,y)] > 0:
        print("kraj "+str(cnt))
        break
    gameEnd = False
    newAduinos = []
    for aduino in aduinos:
        minVal = 99999
        minDir = -1
        ax = aduino[0]
        ay = aduino[1]
        for d in directions:
            tx = ax + dx[d]
            ty = ay + dy[d]
            if 0<=tx<R and 0<=ty<C:
                temp = abs(x - tx) + abs(y - ty)
                if temp < minVal:
                    minVal = temp
                    minDir = d
        aduinosDict[(ax, ay)] -= 1
        ax = ax + dx[minDir]
        ay = ay + dy[minDir]
        if (ax, ay) == (x,y):
            gameEnd = True
            break
        aduinosDict[(ax, ay)] += 1
        newAduinos.append((ax,ay))

    aduinos = []

    deladuinos = set()
    for adu in newAduinos:
        tx = adu[0]
        ty = adu[1]
        if aduinosDict[(tx,ty)] > 1:
            deladuinos.add((tx, ty))
    for adu in newAduinos:
        if adu in deladuinos:
            aduinosDict[adu] = 0
            continue
        aduinos.append(adu)

    if gameEnd:
        print("kraj " + str(cnt))
        break

    cnt += 1
if fin:
    arr[x][y] = "I"
    for adu in aduinos:
        tx = adu[0]
        ty = adu[1]
        arr[tx][ty] = "R"
    
    for i in range(R):
        for j in range(C):
            print(arr[i][j], end="")
        print()