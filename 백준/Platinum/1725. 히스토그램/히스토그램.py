import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def init(heights, tree, node, start, end):
    # 구간별 최소 높이를 가지는 세그먼트 트리
    if start == end:
        tree[node] = start
    else:
        mid = (start + end) // 2
        init(heights, tree, node * 2, start, mid)
        init(heights, tree, node * 2 + 1, mid + 1, end)

        # 최소 높이를 가진 인덱스 저장
        if heights[tree[node*2]] <= heights[tree[node*2 + 1]]:
            tree[node] = tree[node*2]
        else:
            tree[node] = tree[node*2 + 1]


def query(heights, tree, node, start, end, left, right):
    # [left, right] 구간에서 최소 높이를 가진 인덱스 찾기
    if left > end or right < start:
        return -1
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    m1 = query(heights, tree, node * 2, start, mid, left, right)
    m2 = query(heights, tree, node * 2 + 1, mid + 1, end, left, right)

    if m1 == -1:
        return m2
    elif m2 == -1:
        return m1
    else:
        if heights[m1] <= heights[m2]:
            return m1
        else:
            return m2

def get_max(heights, tree, start, end):
    n = len(heights)
    idx = query(heights, tree, 1, 0, n - 1, start, end)

    # 최소 높이 막대를 사용하여 넓이 계산
    area = (end - start + 1) * heights[idx]

    # 최소 높이 막대 왼쪽 부분 확인
    if start <= idx - 1:
        tmp_area = get_max(heights, tree, start, idx-1)
        area = max(tmp_area, area)

    if idx + 1 <= end:
        tmp_area = get_max(heights, tree, idx + 1, end)
        area = max(tmp_area, area)

    return area


n = int(input())
heights = [int(input()) for _ in range(n)]

# 세그먼트 트리 크기 초기화
tree_size = 2 ** (math.ceil(math.log2(n)) + 1)

# 세그먼트 트리 초기화
tree = [0] * tree_size
init(heights, tree, 1, 0, n-1)

# 최대 직사각형 넓이 구하기
result = get_max(heights, tree, 0, n-1)
print(result)