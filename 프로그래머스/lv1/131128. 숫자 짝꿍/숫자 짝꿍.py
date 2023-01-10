from collections import Counter

def solution(X, Y):
    answer = ""
    X = Counter(X)
    Y = Counter(Y)
    
    XY = X & Y 
    
    for i in "987654321":
        num = XY[i]
        answer += i * num
    
    if len(answer) > 0 and XY["0"] > 0 :
        answer += "0" * XY["0"]
    elif len(answer) <= 0 and XY["0"] > 0 :
        answer = "0"
        
    return answer if answer else "-1"
