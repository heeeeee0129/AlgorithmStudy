def solution(sequence, k):
    start, end = 0, len(sequence)
    first, last = 0, 0
    _sum = 0
    
    for i in range(0, len(sequence)):
        _sum += sequence[i]
        last = i
            
        if (_sum > k):
            while (_sum > k):
                _sum -= sequence[first]
                first += 1
                
        if _sum == k and last - first < end - start:
            start = first
            end = last
                
            
        
    return [start, end]
