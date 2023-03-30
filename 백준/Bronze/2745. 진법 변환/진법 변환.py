n, b = input().split()
b = int(b)

notation = dict()

for x in '0123456789' :
    notation[x] = int(x)

for x in range(ord('A'), ord('Z') + 1) :
    notation[chr(x)] = x - ord('A') + 10
    
result = 0
for ch in n :
    result = result * b + notation[ch]

print(result)