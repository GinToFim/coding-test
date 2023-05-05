/*
아이디어 : [n-1][m-1] 출력
알고리즘 : bfs(graph, dx/dy)
자료구조 : queue
*/

#include <bits/stdc++.h>

using namespace std;

int n, m;
int graph[101][101] = {0, };
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int BFS(int x, int y) {
    // 큐 및 시작노드 정의
    queue<pair<int, int>> q;
    q.push({x, y});
    
    // 큐가 빌 때까지
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            // 범위 밖이라면 무시
            if (nx < 0 || ny < 0 || nx >= n || ny >= m)
                continue;
            
            // 지나갈 수 있는 길이라면
            if (graph[nx][ny] == 1) {
                graph[nx][ny] = graph[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }
    
    // 도착 지점 return
    return graph[n-1][m-1];
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    cin >> n >> m;
    
    for (int i = 0; i < n; i++) {
        string row;
        cin >> row;    
        for (int j = 0; j < m; j++) {
            graph[i][j] = row[j] - '0';
        }
    }
    
    int result = BFS(0, 0);
    cout << result << '\n';
    
    return 0;
}