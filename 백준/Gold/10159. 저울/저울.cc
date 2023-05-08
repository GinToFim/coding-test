/*
아이디어 : 
알고리즘 : 플로이드 워셜
*/

#include <bits/stdc++.h>

#define MAX 101

using namespace std;

int n, m;
int graph[MAX][MAX] = {0, };

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    cin >> n >> m;
    
    // 간선 정보 입력
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        graph[a][b] = 1;
    }
        
    // 플로이드 워셜 수행
    for (int k = 1; k < n + 1; k++) {
        for (int a = 1; a < n + 1; a++) {
            for (int b = 1; b < n + 1; b++) {
                // 만약 a > k > b가 비교가 가능하다면 
                if (graph[a][k] && graph[k][b]) graph[a][b] = 1;
            }
        }
    }
    
    // 결과 확인
    for (int i = 1; i < n + 1; i++) {
        int cnt = 0;
        for (int j = 1; j < n + 1; j++) {
            // 주대각선이면 생략
            if (i == j) continue;
            
            // i에서 j로 가는길도 없고, j에서 i로 가는길도 없을 때
            if (!graph[i][j] && !graph[j][i]) cnt++;
        }
        cout << cnt << '\n';
    }
    
    return 0;
}