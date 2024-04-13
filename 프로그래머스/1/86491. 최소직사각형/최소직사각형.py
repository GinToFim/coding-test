# 가로에는 두 변 중 긴 값 -> 중에서 최대값
# 세로에는 두 변 중 짧은 값 -> 중에서 최대값

def solution(sizes):
    return max(max(size) for size in sizes) * max(min(size) for size in sizes)