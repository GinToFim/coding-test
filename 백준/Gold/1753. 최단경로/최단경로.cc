/*
아이디어 : 
알고리즘 : dijkstra(graph, dist_table, inf)
자료구조 : PQ
*/

#include <bits/stdc++.h>

#define INF 1e9
#define MAX 20001

using namespace std;

int n, m, start;
vector<pair<int, int> > graph[MAX];
int dist_table[MAX];

// 다익스트라 알고리즘 정의
void dijkstra(int start) {
    // pq 및 시작노드 정의
    priority_queue<pair<int, int> > pq;
    pq.push({0, start}); // {거리, 노드} 순으로 저장
    dist_table[start] = 0;
    
    // pq가 빌 때까지
    while(!pq.empty()) {
        int dist = -pq.top().first;
        int now = pq.top().second;
        pq.pop();
        
        // 이미 처리된 적이 있다면 무시
        if (dist_table[now] < dist) continue;
        
        // 해당 노드와 인접한 노드들 확인
        for (int i = 0; i < graph[now].size(); i++) {
            int v = graph[now][i].first;
            int d = graph[now][i].second;
            
            int cost = dist + d;
            // 기존 거리보다 갱신 거리가 더 짧다면
            if (cost < dist_table[v]) {
                dist_table[v] = cost;
                pq.push({-cost, v});
            }
        }
        
    }
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    cin >> n >> m >> start;
    
    // 간선 정보 입력
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        
        graph[u].push_back({v, w});
    }
    
    // 거리 테이블 초기화
    fill(dist_table, dist_table + MAX, INF);
    
    // dijkstra 알고리즘 수행
    dijkstra(start);
    
    // 거리 테이블 출력(index 1부터)
    for (int i = 1; i < n + 1; i++) {
        if (dist_table[i] == INF) 
            cout << "INF" << '\n';
        else 
            cout << dist_table[i] << '\n';
    }
    
    return 0; 
}