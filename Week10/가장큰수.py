def solution(numbers):
    answer = ''
    string_array = [str(num) for num in numbers]
    string_array.sort(key=lambda x: x * 3, reverse=True)
    answer = ''.join(string_array)
    if answer[0] == "0":
        return "0"
    return answer