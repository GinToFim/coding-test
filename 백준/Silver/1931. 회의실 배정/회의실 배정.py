import sys
input = sys.stdin.readline

n = int(input())
meetings = []

for _ in range(n) :
	s, e = map(int, input().split()) # start, end
	meetings.append((s, e))

meetings.sort(key=lambda x : (x[1], x[0]))

result = 1
end = meetings[0][1]

for meet in meetings[1:] :
	if meet[0] >= end :
		result += 1
		end = meet[1]

print(result)