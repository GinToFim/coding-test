# 아이디어 : 1. k번만큼 넣었다가 빼기
# 알고리즘 : 
# 자료구조 : queue(deque)

from collections import deque

n, k = map(int, input().split())

queue = deque(x for x in range(1, n + 1))
result = []

# queue가 빌 때까지
while queue :
    # k-1번 만큼 넣었다가 빼기
    for _ in range(k - 1) :
        queue.append(queue.popleft())
    
    now = queue.popleft()
    result.append(now)
    
print("<", end="")
for x in result[:-1] :
    print(x, end=', ')
print(f"{result[-1]}>")