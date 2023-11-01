import math

# 부모노드와 자식노드 확인
def check(num_bin, parent):
    # 현재 이진수가 비어있다면 종료
    if num_bin == '':
        return True
    
    mid = len(num_bin) // 2
    child = num_bin[mid]
    
    # 자식이 존재하는데 부모가 없다면
    if child == '1' and parent == '0':
        return False
    else:
        # 현재 서브 트리의 자식들도 확인
        return check(num_bin[:mid], child) and check(num_bin[mid+1:], child)

# 표현 가능한 이진트리인지 확인
def expressible(num):
    num_bin = bin(num)[2:]
    
    # 포화 이진트리 특징상 (2^n - 1)의 자릿수를 가져야 함
    digit = 2 ** int(math.log2(len(num_bin)) + 1) - 1
    num_bin = "0" * (digit - len(num_bin)) + num_bin
    
    # 자식노드가 존재한다면 부모 노드는 존재해야 함
    # 시작부터는 무조건 존재
    if num_bin[len(num_bin) // 2] == '1' and check(num_bin, '1'):
        return 1
    else:
        return 0
    
    
def solution(numbers):
    answer = [expressible(num) for num in numbers]    
    return answer