# 아이디어 defaultdict 사용 모듈 사용
# 알고리즘 
# 자료구조

from collections import defaultdict
import sys
input = sys.stdin.readline

# value를 int형으로 초기화
bell_dict = defaultdict(int) 
cnt = 0

while True :
	bell = input().rstrip()
	# 빈 문자열이면 탈출
	if bell == '' :
		break
		
	bell_dict[bell] += 1
	cnt += 1

# bell_dict의 key를 리스트로 저장한 후 
# 리스트 정렬
bell_keys = list(bell_dict.keys())
bell_keys.sort()

for key in bell_keys :
	# 백분율 (round 함수 주의)
	rate = bell_dict[key] / cnt * 100
	print(f'{key} {rate:.4f}')