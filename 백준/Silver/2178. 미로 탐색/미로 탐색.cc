// graph, 상하좌우(dx, dy) 정의
// 알고리즘 : bfs
// 자료구조 : queue(deque)

#include <iostream>
#include <string>
#include <queue>
#include <utility>

using namespace std;

int n, m;
int graph[201][201];

// 상하좌우 정의
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int BFS(int x, int y) {
    // 큐 및 시작노드 정의
    queue<pair<int, int>> q;
    q.push({x, y});

    // 큐가 빌 때까지
    while (!q.empty()) {
        x = q.front().first;
        y = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            // 범위 밖이라면 무시
            if (nx < 0 || ny < 0 || nx >= n || ny >= m) 
                continue;

            // 괴물이 없다면(1)
            if (graph[nx][ny] == 1) {
                graph[nx][ny] = graph[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }

    return graph[n-1][m-1];
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        string row;
        cin >> row;

        for (int j = 0; j < m; j++) {
            graph[i][j] = row[j] - '0';
        }
    }

    cout << BFS(0, 0) << '\n';
    return 0;
}