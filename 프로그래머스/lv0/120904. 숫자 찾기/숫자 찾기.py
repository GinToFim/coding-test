def solution(num, k):
    array = [x for x in str(num)]
    
    if str(k) in array :
        return array.index(str(k)) + 1
    else :
        return -1