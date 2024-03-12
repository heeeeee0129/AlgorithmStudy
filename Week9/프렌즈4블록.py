

def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board]
    count = 0
    turn_count = 6
    while turn_count:
        bomb = set()
        turn_count = 0
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == 'X':
                    continue
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    bomb.add((i,j))
                    bomb.add((i+1, j))
                    bomb.add((i+1, j+1))
                    bomb.add((i, j+1))

        turn_count = len(bomb)
        count += turn_count

        for j in range(n):
            stack = []
            for i in range(m-1, -1, -1):
                if (i, j) not in bomb:
                    stack.append(board[i][j])
            count_element = len(stack)
            for i in range(0, m):
                if i < m-count_element:
                    board[i][j] = 'X'
                else:
                    board[i][j] = stack.pop()
    
    return count
            