def solution(number, k):
    stack = []
    remove = 0
    for i in number:
        while stack and stack[-1]<i and remove < k:
            stack.pop()
            remove += 1
        stack.append(i)
    stack = stack[:len(number)-k] # 해당 코드를 넣지 않으니 333222111 같이 줄어드는 테스트케이스에서 기댓값보다 길게 나옴
    answer = ''.join(stack)
    return answer
