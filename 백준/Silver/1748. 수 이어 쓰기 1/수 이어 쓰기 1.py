import sys
input = sys.stdin.readline

n = int(input())
n_len = len(str(n))
result = 0

for i in range(n_len - 1):
    result += 9 * 10 ** i * (i + 1)
    
result += (n - 10 ** (n_len - 1) + 1) * n_len
print(result)