n = int(input())

result = 0
row = [0] * n

def is_check(x) :
	for i in range(x) :
		if row[x] == row[i] or abs(row[x] - row[i]) == (x - i) :
			return False

	return True

def n_queens(x) :
	global result
	if x == n :
		result += 1
		return 

	for i in range(n) :
		row[x] = i 
		if is_check(x) :
			n_queens(x + 1)

n_queens(0)
print(result)