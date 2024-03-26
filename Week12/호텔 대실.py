def solution(book_time):
    answer = 0
    book_time = sorted(book_time)
    
    total = 0
    available = 0
    checkout = []
    
    for book in book_time:
        while checkout and checkout[0] <= book[0]:
            checkout.pop(0)
            available += 1
            
        if available == 0:
            total += 1
        else:
            available -= 1
        
        time = int(book[1][-2:])+10
        if time >= 60:
            time = f"{int(book[1][:2])+1:02}" + ":" + f"{time-60:02}"
        else:  
            time = book[1][:-2] + f"{time:02}"
            
        checkout.append(time)
        checkout = sorted(checkout)
            
    return total
