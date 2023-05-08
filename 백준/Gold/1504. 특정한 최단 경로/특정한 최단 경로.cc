/*
아이디어 : 1. (1 -> v1 -> v2 -> n) VS (1 -> v2 -> v1 -> n) 비교하기
알고리즘 : dijkstra(graph, dist_table, INF)
자료구조 : pq 
*/

#include <bits/stdc++.h>

#define MAX 801
#define INF 1e7

using namespace std;

int n, e;
vector<pair<int, int> > graph[MAX];
int v1, v2;

int dijkstra(int start, int end) {
    // 거리 테이블 정의
    int dist_table[MAX];
    fill(dist_table, dist_table + MAX, INF);
    
    priority_queue<pair<int, int> > pq;
    pq.push({0, start}); // {거리, 노드} 순으로 저장
    dist_table[start] = 0;
    
    // pq가 빌 때까지
    while(!pq.empty()) {
        int dist = -pq.top().first;
        int now = pq.top().second;
        pq.pop();
        
        // 이미 처리된 적이 있다면
        if (dist_table[now] < dist) continue;
        
        // 해당 노드와 인접한 노드들 확인
        for (int i = 0; i < graph[now].size(); i++) {
            int v = graph[now][i].first;
            int d = graph[now][i].second;
            
            int cost = dist + d;
            
            // 갱신 거리가 기존 거리보다 짧다면
            if (cost < dist_table[v]) {
                dist_table[v] = cost;
                pq.push({-cost, v});
            }
        }
        
    }
    return dist_table[end];
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    cin >> n >> e;
    
    // 간선 정보 입력
    for(int i = 0; i < e; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        // 양방향
        graph[a].push_back({b, c});
        graph[b].push_back({a, c});
    }
    
    cin >> v1 >> v2;
    
    // 1 -> v1 -> v2 -> n
    int value1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n);
    int value2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n);
    
    int result = min(value1, value2);
    
    if (result < INF)
        cout << result << '\n';
    else 
        cout << -1 << '\n';
    
    return 0;
}
