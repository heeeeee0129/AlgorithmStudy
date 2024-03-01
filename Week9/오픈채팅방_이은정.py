def solution(record):
    answer = []
    dict = {}
    
    # record를 한 번 돌면서 이름 변경 됐는지 확인 후 변경
    for rec in record:
        check = rec.split(" ")
        if check[0] == 'Enter' or check[0] == 'Change':
            dict[check[1]] = check[2]
    
    # record를 다시 한 번 돌면서 마지막 이름 넣어서 출력
    for rec in record:
        check = rec.split(" ")
        if check[0] == 'Enter':
            answer.append(dict[check[1]] + "님이 들어왔습니다.")
        elif check[0] == 'Leave':
            answer.append(dict[check[1]] + "님이 나갔습니다.")
            
    return answer
