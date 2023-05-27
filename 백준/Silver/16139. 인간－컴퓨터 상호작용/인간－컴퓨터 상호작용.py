# 아이디어 : 딕셔너리를 사용한 누적 합
# 알고리즘 : prefix sum

import sys
input = sys.stdin.readline

string = input().rstrip()

# a - z 까지 0 선언
keyboard = {chr(num) : 0 for num in range(ord('a'), ord('z') + 1)}
dp = [keyboard]

for ch in string:
    keyboard = {key:value for key, value in dp[-1].items()}
    keyboard[ch] += 1
    dp.append(keyboard)
    
q = int(input())
for _ in range(q):
    ch, l, r = input().split()
    l = int(l) + 1
    r = int(r) + 1
    
    print(dp[r][ch] - dp[l-1][ch])