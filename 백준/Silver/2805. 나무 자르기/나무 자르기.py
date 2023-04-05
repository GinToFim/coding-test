import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

# 나무 자르기 함수(이진 탐색)
def cut() :
    start, end = 0, max(trees)

    result = 0
    while start <= end :
        mid = (start + end) // 2
        total = 0
        for tree in trees :
            if tree > mid :
                total += tree - mid
      
        if total >= m :
            result = mid
            start = mid + 1
        else :
            end = mid - 1

    return result

print(cut())