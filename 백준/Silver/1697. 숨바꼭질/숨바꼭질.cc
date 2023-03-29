#include <iostream>
#include <vector>
#include <queue>
#define MAX 100001

using namespace std;

int n, k;
vector<int> board(MAX, -1);

int BFS(int start) {
    // 큐 및 시작노드 정의
    queue<int> q;
    q.push(start);
    board[start] = 0;

    // 큐가 빌 때까지
    while (!q.empty()) {
        int v = q.front();
        q.pop();

        // 도착했다면 return
        if (v == k) 
            break;

        // 범위 이내이고 방문하지 않았다면
        if (v-1 >= 0 && board[v-1] == - 1) {
            board[v-1] = board[v] + 1;
            q.push(v-1);
        }

        if (v+1 < MAX && board[v+1] == - 1) {
            board[v+1] = board[v] + 1;
            q.push(v+1);
        }
        
        if (2*v < MAX && board[2*v] == - 1) {
            board[2*v] = board[v] + 1;
            q.push(2*v);
        }
    }

    return board[k];
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> k;

    int result = BFS(n);
    cout << result << '\n';
    return 0;
}