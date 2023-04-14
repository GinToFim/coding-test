import sys
input = sys.stdin.readline

while True :
    n = int(input())
    
    if n == -1 :
        break
    
    # 약수 처음에 1도 포함
    divisor = [1]
    
    for i in range(2, n) :
        if n % i == 0 :
            divisor.append(i)
    
    if n == sum(divisor) :
        print(f"{n} = ", end='')
        for i in range(len(divisor)-1) :
            print(f"{divisor[i]} + ", end='')
        print(divisor[-1])
    else :
        print(f"{n} is NOT perfect.")