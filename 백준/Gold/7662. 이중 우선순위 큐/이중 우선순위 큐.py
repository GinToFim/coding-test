from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())

    min_hq = []
    max_hq = []
    num_dict = defaultdict(int)

    for _ in range(k):
        op, num = input().split()
        num = int(num)

        # 삽입이라면
        if op == 'I':
            num_dict[num] += 1
            heapq.heappush(min_hq, num)
            heapq.heappush(max_hq, -num)
        # 최소 힙 삭제라면
        elif num == -1: 
            # 최소 힙에 원소가 있으면서, 이미 삭제했다면
            while min_hq and num_dict[min_hq[0]] < 1:
                heapq.heappop(min_hq)

            if min_hq:
                min_val = heapq.heappop(min_hq)
                num_dict[min_val] -= 1
        # 최대 힙 삭제라면
        else:
            # 최대 힙에 원소가 있으면서, 이미 삭제했다면
            while max_hq and num_dict[-max_hq[0]] < 1:
                heapq.heappop(max_hq)
            if max_hq:
                max_val = -heapq.heappop(max_hq)
                num_dict[max_val] -= 1

    # 마지막에 최소 힙, 최대 힙 나머지 삭제
    while min_hq and num_dict[min_hq[0]] < 1:
        heapq.heappop(min_hq)
    while max_hq and num_dict[-max_hq[0]] < 1:
        heapq.heappop(max_hq)

    # 힙큐에 원소가 있다면
    if max_hq and min_hq:
        print(-max_hq[0], min_hq[0])
    else:
        print("EMPTY")