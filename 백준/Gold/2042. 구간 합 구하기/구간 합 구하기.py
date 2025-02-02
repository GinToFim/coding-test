# 아이디어: 1. tree 초기화 (트리의 크기)

# 알고리즘: 세그먼트 트리
# 자료구조: 트리

import math
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
data = [int(input()) for _ in range(n)]

# 세그먼트 트리 초기화
def init_tree(data, n):
    # 트리 사이즈 및 세그먼트 트리 초기화
    tree_size = 2 ** (math.ceil(math.log2(n)) + 1)
    seg_tree = [0] * tree_size

    # 리프 노드에 원본 데이터 넣기
    for i in range(n):
        seg_tree[i + tree_size // 2] = data[i]

    # 리프 노드를 제외한 나머지 값 넣기
    for i in range(tree_size // 2 - 1, 0, -1):
        seg_tree[i] = seg_tree[2*i] + seg_tree[2*i + 1]

    return seg_tree, tree_size

seg_tree, tree_size = init_tree(data, n)

# 세그먼트 트리 질의
def query(seg_tree, tree_size, start, end):
    # 기존 인덱스를 리프 노드 인덱스로 변경
    start += tree_size // 2 - 1
    end += tree_size // 2 - 1
    sum_val = 0

    while start <= end:
        if start % 2 == 1:
            sum_val += seg_tree[start]
        start = (start + 1) // 2

        if end % 2 == 0:
            sum_val += seg_tree[end]
        end = (end - 1) // 2

    return sum_val

# 세그먼트 트리 업데이트
def update(seg_tree, tree_size, idx, val):
    # 기존 인덱스를 리프 노드 인덱스로 변경
    idx += tree_size // 2 - 1
    seg_tree[idx] = val
    
    while idx > 1:
        idx //= 2
        seg_tree[idx] = seg_tree[idx * 2] + seg_tree[idx * 2 + 1]
    
    return seg_tree

for _ in range(m + k):
    a, b, c = map(int, input().split())

    if a == 1:
        seg_tree = update(seg_tree, tree_size, b, c)
    else:
        print(query(seg_tree, tree_size, b, c))