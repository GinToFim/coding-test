import sys
input = sys.stdin.readline

n = int(input())
RGB = []

r, g, b = map(int, input().split())
RGB = [r, g, b]

sub_r, sub_g, sub_b = RGB
for i in range(1, n) :
	r, g, b = map(int, input().split())
	sub_r, sub_g, sub_b = RGB
	RGB[0] = r + min(sub_g, sub_b)
	RGB[1]  = g + min(sub_r, sub_b)
	RGB[2]  = b + min(sub_r, sub_g)
	
print(min(RGB))