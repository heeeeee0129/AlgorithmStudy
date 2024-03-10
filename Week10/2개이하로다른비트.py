def solution(numbers):
    answer = []
    # 짝수이면 +1
    # 홀수이면 가장 끝 0 -> 1 + 그 앞에 1 -> 0
    
    for number in numbers:
        if number % 2 == 0:
            answer.append(number+1)
        else:
            bin_num = list(bin(number)[2:])
            for idx in range(len(bin_num)-1, -1, -1):
                if idx == 0:
                    bin_num[0] = '0'
                    bin_str = "1" + ''.join(bin_num)
                    answer.append(int(bin_str, 2))
                    break
                if bin_num[idx-1] == '0':
                    bin_num[idx-1] = '1'
                    bin_num[idx] = '0'
                    answer.append(int(''.join(bin_num), 2))
                    break
            
    return answer