// 아이디어: 그래프, dxdy, 
// 알고리즘: bfs
// 자료구조: queue

import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = 0;
        int n = maps.length;
        int m = maps[0].length;
        
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
    
        // 큐 및 시작노드 정의
        Queue<Node> queue = new LinkedList<>();
        queue.offer(new Node(0, 0));
        
        // 큐가 빌 때까지
        while (!queue.isEmpty()) {
            Node node = queue.poll();
            int x = node.getX();
            int y = node.getY();
            
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                // 범위 밖이라면 무시
                if (nx < 0 || ny < 0 || nx >= n || ny >= m) 
                    continue;
                
                // 해당 구역을 지나갈 수 있다면
                if (maps[nx][ny] == 1) {
                    maps[nx][ny] = maps[x][y] + 1;
                    queue.offer(new Node(nx, ny));
                } 
            }
        }
        
        if (maps[n-1][m-1] == 1)
            return -1;
        
        return maps[n-1][m-1];
    }
}

class Node {
    private int x;
    private int y;
    
    Node(int x, int y) {
        this.x = x;
        this.y = y;
    }
    
    public int getX() {
        return this.x;
    }
    
    public int getY() {
        return this.y;
    }
}