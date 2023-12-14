# 아이디어: 1. 최대 압축은 len(s) // 2 
#          2. 1 ~ len(s)//2 + 1 에 대한 압축을 완전탐색
#          3. 압축 횟수(count)가 2 이상이라면 str(count) + prev
#                                보다 작다면 prev
# 알고리즘: 문자열, 구현, 완전탐색

def solution(s):
    answer = len(s)
    
    # 압축에 대한 단위(step)
    for step in range(1, len(s) // 2 + 1):
        compressed = "" # 압축을 저장할 문자열
        prev = s[:step]  # 이전 단어
        count = 1 # 압축 횟수 
        
        for j in range(step, len(s), step):
            # 이전 문자와 같다면
            if prev == s[j: j + step]:
                # 압축 늘리기
                count += 1
            else: # 같지 않다면
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j: j + step] # 현재 단어 갱신
                count = 1
                
        # 마지막 단어 처리하기
        compressed += str(count) + prev if count >= 2 else prev
        
        # 압축 단어에 대한 최소 길이 갱신
        answer = min(answer, len(compressed))
        
    return answer