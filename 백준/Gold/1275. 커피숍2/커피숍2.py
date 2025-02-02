import math
import sys
input = sys.stdin.readline

def init_tree(data, n):
    # 트리 사이즈 및 세그먼트 트리 초기화
    tree_size = 2 ** (math.ceil(math.log2(n)) + 1)
    seg_tree = [0] * tree_size

    # 리프 노드 초기화
    for i in range(n):
        seg_tree[i + tree_size // 2] = data[i]

    # 리프 노드를 제외한 나머지 노드 삽입
    for i in range(tree_size //2 - 1, 0, -1):
        seg_tree[i] = seg_tree[2*i] + seg_tree[2*i + 1]

    return seg_tree, tree_size

def query(seg_tree, tree_size, start, end):
    # 세그먼트 트리 인덱스로 변경
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

def update(seg_tree, tree_size, idx, value):
    idx += tree_size // 2 - 1
    seg_tree[idx] = value

    while idx > 1:
        idx //= 2
        seg_tree[idx] = seg_tree[idx * 2] + seg_tree[idx * 2 + 1]
    
    return seg_tree

n, q = map(int, input().split())
data = list(map(int, input().split()))

seg_tree, tree_size = init_tree(data, n)

for _ in range(q):
    x, y, a, b = map(int, input().split())

    if x > y:
        x, y = y, x

    print(query(seg_tree, tree_size, x, y))
    update(seg_tree, tree_size, a, b)