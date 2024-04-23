def solution(data, col, row_begin, row_end):
    sorted_arr = sorted(data, key=lambda x : (x[col-1], -x[0]))
    before = sum(number % (row_begin) for number in sorted_arr[row_begin-1])
    for i in range(row_begin, row_end):
        s_i = sum(number % (i+1) for number in sorted_arr[i])
        before ^= s_i
    return before

