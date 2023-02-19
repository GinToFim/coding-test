import sys
input = sys.stdin.readline

numbers = []

for _ in range(5) :
	numbers.append(int(input()))

numbers.sort()

print(sum(numbers)//5) # 평균값
print(numbers[2]) # 중앙값