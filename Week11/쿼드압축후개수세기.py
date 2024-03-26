def solution(arr):
    answer = [0,0]
    def split(tmp,m,n,length):
        # print("tmp",tmp)
        allZero = True
        allOne = True
        for i in tmp[m:m+length]:
            for j in i[n:n+length]:
                if j == 0:
                    allOne = False
                elif j == 1:
                    allZero = False
                if not allZero and not allOne:
                    break
        if allZero:
            answer[0] += 1
        elif allOne:
            answer[1] += 1
        else:
            origin = int(length/2)
            # print("recursion",origin)
            split(tmp, m, n, origin)
            split(tmp,m,n+origin,origin)
            split(tmp,m+origin,n,origin)
            split(tmp,m+origin,n+origin,origin)

    split(arr,0,0,len(arr))
    return answer
