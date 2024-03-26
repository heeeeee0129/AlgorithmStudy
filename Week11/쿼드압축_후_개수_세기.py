def recur (arr, num):
    # 칸이 하나이면 해당 값에 1을 더하고 return
    if len(arr) == 1:
        num[arr[0]] += 1
        return
    
    # 4칸으로 나누기
    for i in range(0, 2):
        for j in range(0, 2):
            l = (len(arr)//2)
            
            baseNum = arr[l*i][l*j]
            ch = 0
            
            # 모든 칸이 같은지 체크
            for row in range(l*i, l*(i+1)):
                for col in range(l*j, l*(j+1)):
                    if baseNum != arr[row][col]:
                        ch = 1
                        break
                
                if ch == 1:
                    break
            # 모든 칸이 같다면 해당 값의 개수 +1
            if ch == 0:
                num[baseNum] += 1
            # 다르다면 해당 칸은 다시 재귀
            else:
                new = []
                for idx in range(l*i, l*(i+1)):
                    new.append(arr[idx][l*j:l*(j+1)])
                recur(new, num)
            

def solution(arr):
    answer = []
    num = [0, 0]
    # 재귀?
    recur(arr, num)
    
    # 분할하기 전에 다 같은 경우
    if num == [0, 4]:
        num = [0, 1]
    elif num == [4, 0]:
        num = [1, 0]
    return num
