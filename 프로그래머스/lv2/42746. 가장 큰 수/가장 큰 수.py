def solution(numbers):
    numbers.sort(key = lambda num : str(num) * 3, reverse=True)
    answer = ''.join([str(num) for num in numbers])
    
    return str(int(answer))