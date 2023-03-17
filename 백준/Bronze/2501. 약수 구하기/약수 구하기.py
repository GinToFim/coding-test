n, m = map(int, input().split())

def checkDivisor(n, m) :
    cnt = 0 # k 번째 약수
    for x in range(1, n + 1) :
        if n % x == 0 :
            cnt += 1
            if cnt == m :
                return x
                break
    
    # 해당하는 k번째 수가 없다면
    return 0

print(checkDivisor(n, m))