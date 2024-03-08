def solution(numbers):
    answer = []
    for number in numbers:
        # 만약 짝수라면 무조건 다음 수가 제일 작음
        if number % 2 == 0:
            answer.append(number+1)
            continue;
        
        # 만약 홀수라면 맨 앞의 1과 그 앞의 0을 변경
        curr = '0' + bin(number)[2:]   # 현재 수를 이진수로 변환
        
        curr = list(curr)
        
        for idx in range(len(curr)-1, -1, -1):
            if curr[idx] == '0':
                curr[idx+1] = '0'
                curr[idx] = '1'
                curr = ''.join(curr)
                answer.append(int(curr, 2))
                break;
        
    return answer
