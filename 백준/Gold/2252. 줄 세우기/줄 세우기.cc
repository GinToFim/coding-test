/*
아이디어 : 
알고리즘 : topology sort (graph, indegree)
자료구조 : queue
*/

#include <bits/stdc++.h>

#define MAX 40001

using namespace std;

int n, m; 
vector<int> graph[MAX]; // 그래프 초기화
int indegree[MAX]; // 진입차수 초기화
vector<int> result; // 위상 정렬 결과

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	cin >> n >> m;
	
	// 간선 정보 입력
	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		
		// a -> b
		graph[a].push_back(b);
		indegree[b] += 1;
	}
	
	queue<int> q;
	
	// 진입차수가 0인 노드들을 큐에 추가
	for (int i = 1; i < n + 1; i++) {
		if (indegree[i] == 0) q.push(i);
	}
	
	// 큐가 빌 때까지
	while(!q.empty()) {
		int now = q.front();
		q.pop();
		result.push_back(now);
		
		// 해당 노드와 인접한 노드들 진입차수 1씩 빼기
		for (int i = 0; i < graph[now].size(); i++) {
			int v = graph[now][i];
			indegree[v] -= 1;
			
			if (indegree[v] == 0) q.push(v);
		}
	}
	
	for (int i = 0; i < result.size(); i++) 
		cout << result[i] << ' ';
	cout << '\n';
	
	return 0;
}