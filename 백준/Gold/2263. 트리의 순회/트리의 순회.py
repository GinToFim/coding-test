# 아이디어:
# 알고리즘:

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
inorder_pos = [0 for _ in range(n + 1)]

# 전위 순회 함수 정의
def preorder(inorder_s, inorder_e, postorder_s, postorder_e):
    # 재귀 함수 종료 조건 정의
    # 둘 중에 하나라 start 인덱스가 end보다 크다면
    if (inorder_s > inorder_e) or (postorder_s > postorder_e):
        return 
    
#     print(inorder_s, inorder_e, postorder_s, postorder_e)
    # 후위 순회의 마지막 노드 출력 = (루트 노드)
    root = postorder[postorder_e]
    print(root, end=' ')
    
    # 루트 노드가 중위 순회에서 어디에 위치했는지 찾기
    # 왼쪽 서브 트리와 오른쪽 서브 트리의 길이 구하기
    left = inorder_pos[root] - inorder_s
    right = inorder_e - inorder_pos[root]
    
    # 왼쪽 서브 트리
    preorder(inorder_s, inorder_s + left - 1, postorder_s, postorder_s + left - 1)
    # 오른쪽 서브 트리
    preorder(inorder_e - right + 1, inorder_e, postorder_e - right, postorder_e - 1)
    

# 후위순회의 마지막 값이 중위순회 몇 번째에 존재하는지
# 중위 순회의 위치들을 따로 기억
for i in range(n):
    inorder_pos[inorder[i]] = i
    
preorder(0, n-1, 0, n-1)