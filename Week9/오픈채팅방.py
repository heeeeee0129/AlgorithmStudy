def solution(record):
    answer = []
    dict = {}
    for idx, val in enumerate(record):
        data = val.split()
        if data[0] == "Enter" or data[0] == "Change":
            dict[data[1]] = data[2]
    for idx, val in enumerate(record):
        data = val.split()
        if data[0] == "Enter":
            answer.append(dict[data[1]]+"님이 들어왔습니다.")
        elif data[0] == "Leave":
            answer.append(dict[data[1]]+"님이 나갔습니다.")
    return answer
