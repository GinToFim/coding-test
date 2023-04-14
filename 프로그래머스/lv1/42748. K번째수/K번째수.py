def solution(array, commands):
    answer = []
    
    for command in commands :
        i, j, k = command
        short_array = array[i-1:j]
        short_array.sort()
        
        answer.append(short_array[k-1])
    
    return answer