city_number = int(input())
line_length = list(map(int, input().split()))
oil_price = list(map(int, input().split()))
min_price = oil_price[0]
total = 0
for i in range(len(line_length)):
    if oil_price[i] >= min_price:
        total += min_price * line_length[i]
    elif oil_price[i] < min_price:
        min_price = oil_price[i]
        total += min_price * line_length[i]
print(total)