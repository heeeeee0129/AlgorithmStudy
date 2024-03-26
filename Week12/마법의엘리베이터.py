def solution(storey):
    answer = 0
    tmp = list(map(int,list(str(storey))))
    list_story = []
    for i in reversed(tmp):
        list_story.append(i)
    idx = 0
    while True:
        if idx >= len(list_story):
            break
        val = list_story[idx]
        if val < 5:
            list_story[idx] = 0
            answer += val
        elif val == 5:
            if idx < len(list_story)-1 and list_story[idx+1] < 5:
                list_story[idx] = 0
                answer += val
            elif idx < len(list_story)-1 and list_story[idx+1] >= 5:
                list_story[idx] = 0
                answer += 10-val
                list_story[idx+1] += 1
            elif idx == len(list_story) -1:
                answer += 5
                list_story[idx] = 0
        elif val > 5: 
            if idx == len(list_story) -1:
                list_story.append(1)
            else:
                list_story[idx+1] += 1
            answer += 10-val
            list_story[idx] = 0
        idx += 1
    return answer
