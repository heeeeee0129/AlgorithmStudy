def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board]
    
    # 없애야 하는 것이 더이상 없을 때까지 반복
    while 1:
        re = []
        # 1. 없애야 할 것들 확인
        for rowIdx in range(m-1):
            for colIdx in range(n-1):
                if board[rowIdx][colIdx] != 0 and board[rowIdx][colIdx] == board[rowIdx][colIdx+1] and board[rowIdx][colIdx] == board[rowIdx+1][colIdx] and board[rowIdx][colIdx] == board[rowIdx+1][colIdx+1]:
                    if [rowIdx, colIdx] not in re:
                        re.append([rowIdx, colIdx])
                    if [rowIdx, colIdx+1] not in re:
                        re.append([rowIdx, colIdx+1])
                    if [rowIdx+1, colIdx] not in re:
                        re.append([rowIdx+1, colIdx])
                    if [rowIdx+1, colIdx+1] not in re:
                        re.append([rowIdx+1, colIdx+1])
                    

        # 2. 없애야 할 것들 없애기
        # 없애야 할 것이 없는 경우 while문 탈출
        if re == []:
            break;
        
        answer += len(re)
        
        for word in re:
            board[word[0]][word[1]] = 0
        
        # 3. 비어있는 공간으로 값 내리기
        for rowIdx in range(m-1, 0, -1):
            for colIdx in range(n):
                i = 1
                
                while board[rowIdx][colIdx] == 0 and rowIdx >= i:
                    if board[rowIdx-i][colIdx] != 0:
                        board[rowIdx-i][colIdx], board[rowIdx][colIdx] = board[rowIdx][colIdx], board[rowIdx-i][colIdx]
                    i += 1
                    
    return answer
