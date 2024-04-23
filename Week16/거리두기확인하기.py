def solution(places):
    answer = []
    row = [[1,1,0],[1,1,0],[-1,-1,0],[-1,-1,0]]
    col = [[0,1,1],[0,-1,-1],[0,1,1],[0,-1,-1]]
    for i in places: # 대기실 개수
        isViolate = False
        for j in range(5): # 하나의 대기실
            for l in range(5): 
                if i[j][l] == 'P': # 응시자일 경우만 사방 체크
                    for k in range(4):
                        hasP = False
                        allX = True
                        for o in range(3):
                            m = j+row[k][o]
                            n = l+col[k][o]
                            if -1<m<5 and -1<n<5:
                                if i[m][n] == 'P':
                                    hasP = True
                                    if abs(row[k][o]) + abs(col[k][o]) < 2:
                                        isViolate = True
                                        break
                                elif i[m][n] == 'O':
                                    allX = False
                                    if abs(row[k][o]) + abs(col[k][o]) == 1:
                                        if abs(row[k][o]) == 1 and -1<m+row[k][o]<5 and i[m+row[k][o]][n] == 'P':
                                            isViolate = True
                                            break
                                        elif abs(col[k][o]) == 1 and -1<n+col[k][o]<5 and i[m][n+col[k][o]] == 'P':
                                            isViolate = True
                                            break
                        if hasP and not allX:  # 지금 조건의 모순은 [PX],[PX] 는 통과시켜버림
                            isViolate = True
                            break
                if isViolate:
                    break
            if isViolate:
                break
        if isViolate:
            answer.append(0)
        else:
            answer.append(1)
                
    return answer
