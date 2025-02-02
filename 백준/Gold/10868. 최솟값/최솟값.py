import math
import sys
input = sys.stdin.readline
INF = int(1e10)

n, m = map(int, input().split())
data = [int(input()) for _ in range(n)]

def init_tree(data, n):
    # 트리 크기 및 세그먼트 트리 초기화
    tree_size = 2 ** (math.ceil(math.log2(n)) + 1)
    seg_tree = [INF] * tree_size

    # 리프 노드 초기화
    for i in range(n):
        seg_tree[i + tree_size // 2] = data[i]
    
    # 리프 노드를 제외한 나머지 값 넣기
    for i in range(tree_size // 2 - 1, 0, -1):
        seg_tree[i] = min(seg_tree[2 * i], seg_tree[2 * i + 1])

    return seg_tree, tree_size

def query(seg_tree, tree_size, start, end):
    # 세그먼트 트리 인덱스로 변경
    start += tree_size // 2 - 1
    end += tree_size // 2 - 1
    min_val = INF

    while start <= end:
        if start % 2 == 1:
            min_val = min(min_val, seg_tree[start])
        start = (start + 1) // 2

        if end % 2 == 0:
            min_val = min(min_val, seg_tree[end])
        end = (end - 1) // 2
    
    return min_val

seg_tree, tree_size = init_tree(data, n)

for _ in range(m):
    a, b = map(int, input().split())

    print(query(seg_tree, tree_size, a, b))