def recur (p):
    if not p:
        return ""
    
    k = 2
    u, v = '', ''
    while True:
        if p[:k].count('(') == p[:k].count(')'):
            u = p[:k]
            v = p[k:]
            break;
        k += 2
        
    if u[0] == '(':
        return u + recur(v)
    else:
        return "(" + recur(v) + ")" + ''.join(['(' if c == ')' else ')' for c in u[1:-1]])



def solution(p):
    
    return recur(p)
