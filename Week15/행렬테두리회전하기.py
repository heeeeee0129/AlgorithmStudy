def solution(rows, columns, queries):
    answer = []
    arr = [[0]*columns for _ in range(rows)]
    idx = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = idx
            idx += 1
    for x1, y1, x2, y2 in queries:
        min_value = 1e9
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        temp = arr[x1][y1]
        min_value = min(min_value, temp)
        for i in range(x1, x2):
            arr[i][y1] = arr[i+1][y1]
            min_value = min(min_value, arr[i][y1])
        for i in range(y1, y2):
            arr[x2][i] = arr[x2][i+1]
            min_value = min(min_value, arr[x2][i])
        for i in range(x2, x1, -1):
            arr[i][y2] = arr[i-1][y2]
            min_value = min(min_value, arr[i][y2])
        for i in range(y2, y1+1, -1):
            arr[x1][i] = arr[x1][i-1]
            min_value = min(min_value, arr[x1][i])
        arr[x1][y1+1] = temp
        answer.append(min_value)
    return answer