class Solution {
    
    int answer = 0;
    
    public int solution(int[] numbers, int target) {
        dfs(0, numbers, target, 0);
        return answer;
    }
    
    private void dfs(int depth, int[] numbers, int target, int sumValue) {
        // 종료조건 정의
        if (depth == numbers.length) {
            if (sumValue == target) {
                answer += 1;
            }
            return;
        }
        
        dfs(depth + 1, numbers, target, sumValue + numbers[depth]);
        dfs(depth + 1, numbers, target, sumValue - numbers[depth]);
    }
}