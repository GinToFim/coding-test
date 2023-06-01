# 아이디어 : path (문자열)을 활용하여 이전 길 담기
# 알고리즘 : dp 

n = int(input())
dp = [0 for _ in range(n + 1)]
path = ["" for _ in range(n + 1)]
path[1] = "1"

for i in range(2, n + 1):
    dp[i] = dp[i-1] + 1
    past = i - 1
    
    # 3으로 나눌 수 있으면서 3으로 나누는 것이 더 적을 때
    if i % 3 == 0 and dp[i//3] + 1 < dp[i]:
        dp[i] = dp[i//3] + 1
        past = i // 3
    
    # 2로 나눌 수 있으면서 2로 나누는 것이 더 적을 때
    if i % 2 == 0 and dp[i//2] + 1 < dp[i]:
        dp[i] = dp[i//2] + 1
        past = i // 2
        
    path[i] = str(i) + " " + path[past]

print(dp[n])
print(path[n])