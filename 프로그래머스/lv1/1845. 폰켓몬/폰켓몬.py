# 아이디어 : 최대한 많은 종류의 폰켓몬
# 자료구조 : set 자료형으로 중복 제거
# min으로 비교

def solution(nums):
    return min(len(nums)//2, len(set(nums)))