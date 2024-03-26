def solution(n):
    answer = []
    arr = []
    for i in range(n):
        tmp = [-1]*(i+1)
        arr.append(tmp) # 총 필요한 개수만큼 배열 미리 생성
    x, y = 0, 0
    arr[0][0] = 1
    num = 2
    move = n - 1 # 이동하는 횟수
    isFirst = True # 가장 끝 줄일 경우 이동해야하는 카운트가 다르기 때문에 플래그로 분기 조절
    while move > 0:
        for i in range(1,move+1):
            arr[y+i][x] = num
            num += 1
        y += move
        if not isFirst:
            move -= 1
        for i in range(1,move+1):
            arr[y][x+i] = num
            num += 1
        x += move
        move -= 1
        for i in range(1,move+1):
            arr[y-i][x-i] = num
            num += 1
        x -= move
        y -= move
        move -= 1
        isFirst = False # 한 번 돌 경우 이제 제일 끝 줄이 아니니 False 처리
        
    for i in arr:
        for j in i:
            answer.append(j) # 반복문 돌며 answer에 값 더해주기
    return answer
