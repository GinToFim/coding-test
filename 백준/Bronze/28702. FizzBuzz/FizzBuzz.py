a = input()
b = input()
c = input()

if str(a).isdigit():
    b = int(a) + 1
    c = int(b) + 1

if str(b).isdigit():
    c = int(b) + 1

d = int(c) + 1

if d % 15 == 0:
    print("FizzBuzz")
elif d % 5 == 0:
    print("Buzz")
elif d % 3 == 0:
    print("Fizz")
else:
    print(str(d))