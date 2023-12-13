# 아이디어: 1. 최대 압축은 (길이 // 2)만큼 가능
#          2. 완전 탐색으로 1 ~ (길이 // 2)만큼 압축 전부 확인
#          3. 이전 문자열과 같으면 count 1 추가
# 알고리즘: 구현, 문자열 (s의 길이가 1,000이기 때문에 완전탐색 가능)

def solution(s):
    answer = len(s) # 최대 길이로 초기화
    
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[:step] # 첫 문자열 초기화(for. 이전 문자열 기억)
        count = 1 # 압축 횟수
        
        # step 만큼 증가시키며 이전 단어와 비교
        for j in range(step, len(s), step):
            # 이전 단어와 동일하다며 압축 횟수 증가
            if prev == s[j: j + step]:
                count += 1
            # 다른 문자열이 나왔다면
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j: j + step] # 이전 단어 갱신
                count = 1 
        
        # 마지막 남아 있는 문자열 처리
        compressed += str(count) + prev if count >= 2 else prev
        
        # 만들어지는 압축 문자열 중 최소 길이 
        answer = min(answer, len(compressed))
        
    return answer