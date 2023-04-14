def solution(sizes):
    # 가로(두 변중 긴 길이) * 세로(두 변중 짧은 길이)
    return max([max(size) for size in sizes]) * max([min(size) for size in sizes])