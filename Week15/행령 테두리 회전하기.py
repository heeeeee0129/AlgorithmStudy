def solution(rows, columns, queries):
    answer = []
    l = [[i+columns*j for i in range(1, columns+1)] for j in range(0, rows)]

    for query in queries:
        startX, startY = query[1]-1, query[0] - 1
        endX, endY = query[3]-1, query[2]-1
        
        min_val = l[startY][startX]
        prev = l[startY][startX]
        
        currX, currY = startX, startY
        direction = 'right'
        
        while True:
            n = l[currY][currX]
            l[currY][currX] = prev
            if n < min_val:
                min_val = n
            
            if direction == 'right':
                if currX == endX and currY == startY:
                    currY += 1
                    direction = 'down'
                else:
                    currX += 1
            elif direction == 'down':
                if currX == endX and currY == endY:
                    currX -= 1
                    direction = 'left'
                else:
                    currY += 1
            elif direction == 'left':
                if currX == startX and currY == endY:
                    currY -= 1
                    direction = 'up'
                else:
                    currX -= 1
            elif direction == 'up':
                if currX == startX and currY == startY:
                    break
                else:
                    currY -= 1

            prev = n
            
        l[currY][currX] = prev
        answer.append(min_val)

    return answer
