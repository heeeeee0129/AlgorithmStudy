def solution(record):
    answer = []
    dict = {}
    for r in record:
        record_list = r.split()
        if record_list[0] == "Enter":
            if record_list[1] not in dict:
                dict[record_list[1]] = record_list[2]
            else:
                dict[record_list[1]] = record_list[2]
        elif record_list[0] == "Change":
            dict[record_list[1]] = record_list[2]
    
    for r in record:
        record_list = r.split()
        if record_list[0] == "Enter":
            answer.append(f"{dict[record_list[1]]}님이 들어왔습니다.")
        elif record_list[0] == "Leave":
            answer.append(f"{dict[record_list[1]]}님이 나갔습니다.")
    
    return answer