n, b = map(int, input().split())

notation = dict()

for x in range(10) :
    notation[x] = str(x)

for x in range(ord('A'), ord('Z') + 1) :
    key = x - ord('A') + 10
    notation[key] = chr(x)
    
result = ''

while n > 0 :
    result += notation[n % b]
    n //= b

print(result[::-1])