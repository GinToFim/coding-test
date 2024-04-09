# 아이디어:
# 알고리즘: 정렬, ["101", "101010"]에 대한 정렬 비교

def solution(numbers):
    numbers.sort(key = lambda x: str(x) * 3, reverse=True)
    result = "".join(str(num) for num in numbers)
    result = str(int(result))
    
    return result