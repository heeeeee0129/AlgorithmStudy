import datetime
def solution(m, musicinfos):
    poss = [] # 가능한 인덱스 넣기, 추후 인덱스로 재생된 시간 비교, 순서 비교
    music = []
    tmp_m = list(m)
    for i in range(len(tmp_m)):
        if tmp_m[i] == '#':
            tmp_m[i] = ' '
            tmp_m[i-1] = tmp_m[i-1].lower()
    tmp_m = ''.join(tmp_m)
    m = tmp_m.replace(' ','')
    
    for i in musicinfos:
        tmp = i.split(',')
        string = list(tmp[3])
        for j in range(len(string)):
            if '#' in string[j]:
                string[j-1] = string[j-1].lower()
                string[j] = ' '
        string = ''.join(string).replace(' ','')
        tmp[3] = string
        music.extend(tmp)
    for i in range(0,len(music),4):
        start = datetime.datetime.strptime(music[i],"%H:%M")
        end = datetime.datetime.strptime(music[i+1],"%H:%M")
        diff = (end-start).seconds//60
        tmp = music[i+3] *(diff//len(music[i+3]))
        if diff%len(music[i+3]) != 0:
            tmp += music[i+3][:(diff%len(music[i+3])+1)]
        if m in tmp:
            poss.append(i)
    if len(poss) == 1:
        answer = music[poss[0]+2]
    elif len(poss) == 0:
        answer = "(None)"
    else:
        length = 0
        for i in poss:
            start = datetime.datetime.strptime(music[i],"%H:%M")
            end = datetime.datetime.strptime(music[i+1],"%H:%M")
            diff = (end-start).seconds//60 
            if length < diff:
                length = diff
                answer = music[i+2]
    return answer
