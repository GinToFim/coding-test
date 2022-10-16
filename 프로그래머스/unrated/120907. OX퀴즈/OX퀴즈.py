def calculate(X, op, Y, Z) :
    X, Y, Z = int(X), int(Y), int(Z)
    if op == '+' :
        return (X + Y == Z)
    else :
        return (X - Y == Z)

def solution(quiz):
    answer = []
    
    for q in quiz :
        X, op, Y, _, Z = q.split()
        if calculate(X, op, Y, Z) :
            answer.append('O')
        else :
            answer.append('X')
        
    return answer