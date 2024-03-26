def solution(numbers):
    numbers=list(map(str,numbers))
    # 예를 들어, 1이 110보다 크게 나오려면 111과 110110110을 비교해주면 된다.
    numbers = sorted(numbers, key=lambda x: x*3, reverse=True)

    answer = ''.join(numbers)
    return answer if int(answer) != 0 else "0"
