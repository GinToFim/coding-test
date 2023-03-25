// 아이디어 : graph, 상하좌우(dx, dy) 정의
// 알고리즘 : bfs
// 자료구조 : queue

#include <iostream>
#include <queue>
#include <utility>
#include <algorithm>
#include <vector>

using namespace std;

int n;
int graph[26][26];
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
vector<int> result;

int BFS(int x, int y) {
    // 큐 및 시작노드 정의
    queue<pair<int, int>> q;
    q.push({x, y});
    graph[x][y] = 0;
    int cnt = 1; // 아파트 단지 수

    // 큐가 빌 때까지
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            // 범위 밖이라면 무시
            if (nx < 0 || ny < 0 || nx >= n || ny >= n) 
                continue;

            if (graph[nx][ny] == 1) {
                graph[nx][ny] = 0;
                q.push({nx, ny});
                cnt++;
            } 

        }
    }

    return cnt;
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    for (int i = 0; i < n; i++) {
        string row;
        cin >> row;
        for (int j = 0; j < n; j++) 
            graph[i][j] = row[j] - '0';
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (graph[i][j] == 1) {
                int cnt = BFS(i, j);
                result.push_back(cnt);
            }
        }
    }

    // 단지 수 오름차순 정렬
    sort(result.begin(), result.end());

    cout << result.size() << '\n';
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << '\n';
    }
    return 0;
}