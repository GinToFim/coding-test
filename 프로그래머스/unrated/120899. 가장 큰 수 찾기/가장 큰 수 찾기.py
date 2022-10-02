def solution(array):
    answer = []
    max_value = max(array)
    max_idx = array.index(max_value)
    
    answer.append(max_value)
    answer.append(max_idx)
    return answer