# 아이디어 : 1. 오름차순 정렬
#            2. for문으로 맨 앞 원소 하나씩 뽑기
#            3. 나머지 배열을 투 포인터를 이용하여 2개 뽑기
# 알고리즘 : two pointer, sort, brute force

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

# 오름차순 정렬
data.sort()

# 맨 앞 하나만 뽑기
def two_pointer(data) :
    min_value = 4 * int(1e9)
    for i in range(n-2):
        start, end = i + 1, n - 1

        # 투 포인터 알고리즘 실행
        while start < end :
            hap = data[i] + data[start] + data[end]

            if abs(hap) < min_value :
                min_value = abs(hap)
                three_values = [data[i], data[start], data[end]]

                if hap == 0 :
                    return three_values

            # hap 이 음수라면
            if hap < 0 :
                start += 1
            else :
                end -= 1
    
    return three_values
                    
result = two_pointer(data)
print(*result)