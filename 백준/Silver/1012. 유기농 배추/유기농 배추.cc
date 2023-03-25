// 아이디어 : graph, 상하좌우(dx, dy) 정의
// 알고리즘 : BFS
// 자료구조 : queue

#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int T, n, m, k;
int graph[51][51];
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

void BFS(int x, int y) {
    // 큐 및 시작노드 정의
    queue<pair<int, int>> q;
    q.push({x, y});
    graph[x][y] = 0; // 현재 부분 0으로 변경

    // 큐가 빌 때까지
    while(!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            // 범위 밖이라면 무시
            if (nx < 0 || ny < 0 || nx >= n || ny >= m) 
                continue;
            
            if (graph[nx][ny] == 1) {
                graph[nx][ny] = 0;
                q.push({nx, ny});
            }
        }

    }

}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> T;

    while (T--) {
        cin >> m >> n >> k;

        graph[51][51] = {0, }; // 그래프 초기화

        for (int i = 0; i < k; i++) {
            int y, x;
            cin >> y >> x;
            graph[x][y] = 1;
        }

        int result = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == 1) {
                    BFS(i, j);
                    result++;
                }
            }
        }
        cout << result << '\n';
    }
    return 0;
}
