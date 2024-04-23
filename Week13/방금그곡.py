def solution(m, musicinfos):
    dict = {"C#" : "X", "D#" : "Y", "F#": "Z", "G#": "K", "A#": "M", "B#" : "W"}
    for key, value in dict.items():
            m = m.replace(key, value)

    answer = ''
    res_time = 0
    for musicinfo in musicinfos:
        start_time, end_time, title, melody = musicinfo.split(",")
        start_h, start_m = map(int, start_time.split(":"))
        end_h, end_m = map(int, end_time.split(":"))
        time = ( end_h - start_h ) * 60 + end_m - start_m
        if len(m) > time:
            continue

        for key, value in dict.items():
            melody = melody.replace(key, value)

        res = melody

        while len(res) < time:
            res += melody

        melody = res[:time]

        if m in melody and res_time < time:
            answer = title
            res_time = time


    return answer if answer else "(None)"