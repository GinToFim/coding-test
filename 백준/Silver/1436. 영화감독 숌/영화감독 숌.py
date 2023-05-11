# 아이디어
# 알고리즘 : 브루트 포스(n = 10000)

n = int(input())

cnt = 0
num = 0

while (cnt < n):
    num += 1
    if ('666' in str(num)):
        cnt += 1

print(num)