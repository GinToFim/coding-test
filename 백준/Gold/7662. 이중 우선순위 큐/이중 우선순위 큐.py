import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())

    visited = [False] * k
    max_hq = []
    min_hq = []

    for i in range(k):
        op, num = input().split()
        num = int(num)

        if op == 'I':
            heapq.heappush(max_hq, (-num, i)) # 최대힙 삽입
            heapq.heappush(min_hq, (num, i)) # 최대힙 삽입
            visited[i] = True
        elif num == -1: # 최소 힙 삭제
            # 최소 힙에 원소가 있으면서 맨 앞이 이미 없다면
            while min_hq and not visited[min_hq[0][1]]:
                heapq.heappop(min_hq)
            # 최소 힙에 원소가 있다면
            if min_hq:
                visited[min_hq[0][1]] = False
                heapq.heappop(min_hq)
        else: # 최대 힙 삭제
            # 최대 힙에 원소가 있으면서 맨 앞이 이미 없다면
            while max_hq and not visited[max_hq[0][1]]:
                heapq.heappop(max_hq)
            # 최대 힙에 원소가 있다면
            if max_hq:
                visited[max_hq[0][1]] = False
                heapq.heappop(max_hq)


    # 마지막에 최소 힙, 최대 힙 나머지 삭제
    while min_hq and not visited[min_hq[0][1]]:
        heapq.heappop(min_hq)
    while max_hq and not visited[max_hq[0][1]]:
        heapq.heappop(max_hq)

    # 원소가 있다면
    if min_hq and max_hq:
        print(-max_hq[0][0], min_hq[0][0])
    else:
        print("EMPTY")
