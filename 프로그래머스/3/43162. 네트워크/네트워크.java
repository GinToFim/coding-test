// 아이디어: visited 테이블 + 너비 우선탐색 하기
// 알고리즘: bfs
// 자료구조: queue

import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        
        for (int i = 0; i < n; i++) {
            visited[i] = false;
        }
        
        for (int i = 0; i < n; i++) {
            // 한 번도 방문한 적이 없다면
            if (!visited[i]) {
                bfs(n, i, computers, visited);
                answer += 1;
            }
        }
        
        return answer;
    }
    
    public void bfs(int n, int start, int[][] computers, boolean[] visited) {
        // 큐 및 시작 노드 정의
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);
        visited[start] = true;
        
        while (!queue.isEmpty()) {
            int now = queue.poll();

            for (int i = 0; i < n ; i++) {
                // 한 번도 방문한 적이 없으면서 연결되어 있다면
                if (!visited[i] && computers[now][i] == 1) {
                    queue.offer(i);
                    visited[i] = true;
                }
            }
        }
        
    }
}