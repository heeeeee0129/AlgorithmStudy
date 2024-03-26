import datetime
def solution(book_time):
    answer = 0
    book_time.sort()
    room = []
    room.append(book_time[0])
    for i in range(1,len(book_time)):
        inTime = book_time[i][0]
        outTime = book_time[i][1]
        for j in range(len(room)):
            time = datetime.datetime.strptime(room[j][1],"%H:%M")
            diff = (datetime.datetime.strptime(inTime,"%H:%M")-time).seconds//60
            if diff >= 10 and inTime > room[j][1]: # 들어올 시각과 기존 방이 나갈 시각이 차이가 10분 이상 나고 들어올 시각이 더 이후인 경우에만 객실 재사용 가능
                # print("diff",diff,inTime,outTime,room[j][1])
                room[j][0] = inTime
                room[j][1] = outTime
                break
            else:
                if j == len(room) -1:
                    # print("room add")
                    room.append([inTime, outTime])
    answer = len(room)
    return answer

# 개선방향.. 비교할 때 +-10분을 해야할 거 같은데 23:50분 부터는 +10 할 때 문제 발생, 00:9분까지는 -10 할 때 문제 발생..
