# b, d의 최소공배수 구하기

# a  c
# -  -
# b  d

def GCD(a, b) :
    while b > 0 :
        a, b = b, a % b
    
    return a

a, b = map(int, input().split())
c, d = map(int, input().split())

e, f = a*d + b*c, b*d
g = GCD(e, f)

e //= g
f //= g

print(e, f)