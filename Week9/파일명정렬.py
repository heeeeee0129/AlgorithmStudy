def solution(files):
    answer = []
    arr = []
    for idx, file in enumerate(files):
        i = 0
        head = []
        while i < len(file) and not file[i].isdigit():
            head.append(file[i])
            i += 1
        number = []
        while i < len(file) and file[i].isdigit():
            number.append(file[i])
            i += 1
        
        arr.append(["".join(head).lower(), int("".join(number)), idx])
        
    arr = sorted(arr)
    for a in arr:
        answer.append(files[a[2]])

    return answer