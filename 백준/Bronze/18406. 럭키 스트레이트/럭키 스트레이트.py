# 아이디어: 왼쪽(:n//2) 오른쪽(n//2:)의 자릿수 구하기
# 알고리즘: 구현

import sys
input = sys.stdin.readline

string = input().rstrip()
n = len(string)

left = string[:n//2]
right = string[n//2:]

# 왼쪽과 오른쪽에 합이 같다면
if sum(int(ch) for ch in left) == sum(int(ch) for ch in right):
    print("LUCKY")
else:
    print("READY")