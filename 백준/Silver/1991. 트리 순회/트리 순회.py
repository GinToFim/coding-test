# 아이디어: 1. dict[root] = [left, right]
# 알고리즘: 트리
# 자료구조: dict, list

import sys
input = sys.stdin.readline

n = int(input())
tree = dict()

for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]
    
# 전위 순회 정의
def preorder(root):
    # 현재 노드가 null이 아니라면
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])
        
# 중위 순회 정의
def inorder(root):
    # 현재 노드가 null이 아니라면
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])
        
# 후위 순회 정의
def postorder(root):
    # 현재 노드가 null이 아니라면
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')
        
preorder("A")
print()
inorder("A")
print()
postorder("A")
print()