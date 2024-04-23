def solution(m, n, board):
    answer = 0
    board = list(map(list, board))
    while True:
        removeList = []
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == '':
                    continue
                if board[i][j] == board[i+1][j] and board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j+1]:
                    removeList.append((i,j))
                    removeList.append((i+1,j))
                    removeList.append((i,j+1))
                    removeList.append((i+1,j+1))

        if len(removeList) == 0:
            break
        else:
            answer += len(set(removeList))
            for i in removeList:
                x,y = i[0], i[1]
                board[x][y] = ''
                
            for i in reversed(removeList):  
                removed = i[0] - 1
                blank = i[0]
                
                while removed >= 0:       
                    if board[blank][i[1]] == '' and board[removed][i[1]] != '':
                        board[blank][i[1]] = board[removed][i[1]]
                        board[removed][i[1]] = ''
                        blank -= 1

                    removed -= 1
    return answer
