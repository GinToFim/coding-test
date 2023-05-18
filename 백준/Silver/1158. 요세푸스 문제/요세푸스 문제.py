n, k = map(int, input().split())

# 인덱스를 맞추기 위하여 0도 추가
data = [x for x in range(1, n + 1)]

cnt = 0 # data를 pop할 인덱스 순서
result = [] # 요세푸스 결과 리스트

# 리스트가 빌 때까지
while data :
    cnt = (cnt + k - 1) % len(data)
    result.append(data.pop(cnt))

print("<" + ", ".join(map(str, result)) + ">")