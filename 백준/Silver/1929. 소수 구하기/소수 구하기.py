m, n = map(int, input().split())
array = [True for i in range(n + 1)]
array[1] = False # 1은 소수가 X

for i in range(2, int(n ** 0.5) + 1) :
    if array[i] == True :
        for j in range(2 * i, n + 1, i) :
            array[j] = False

for i in range(m, n + 1) :
    if array[i] :
        print(i)