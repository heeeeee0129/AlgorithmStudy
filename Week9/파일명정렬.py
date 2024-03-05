def solution(files):
    answer, li = [], []
    for i in files:
        isNumber = False
        first, last = -1, -1
        for idx, val in enumerate(i):
            if val.isdigit():
                if not isNumber:
                    isNumber = True
                    first = idx
            else:
                if isNumber:
                    last = idx
                    isNumber = False
                    break
        head = i[:first]
        lowerHead = i[:first].lower()
        if last == -1:
            numberTxt = i[first:]
            number = int(i[first:])
            tail = ''
        else:
            numberTxt = i[first:last]
            number = int(i[first:last])
            tail = i[last:]
        li.append((head,lowerHead,numberTxt,number,tail))
    li.sort(key = lambda x: (x[1], x[3]))
    for i in li:
        answer.append(i[0]+i[2]+i[4])
    return answer
