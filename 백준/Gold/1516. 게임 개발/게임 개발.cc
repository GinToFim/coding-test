/*
아이디어 :
알고리즘 : topology sort(graph, indegree)
자료구조 : queue
*/

#include <bits/stdc++.h>

#define MAX 501

using namespace std;

int n;
vector<int> graph[MAX]; // 그래프
int indegree[MAX]; // 진입차수

int times[MAX]; // 현재 비용
int result[MAX]; // 총 비용

void topologySort(void) {
	queue<int> q;
	
	// 총 비용 초기화
	for (int i = 1; i < n + 1; i++)
		result[i] = times[i];
	
	// 진입차수가 0인 노드 q에 추가
	for (int i = 1; i < n + 1; i++)
		if (indegree[i] == 0) q.push(i);
	
	// 큐가 빌 때까지
	while(!q.empty()) {
		int now = q.front();
		q.pop();
		
		// 해당 노드와 인접한 노드들 진입차수 1씩 빼기
		for (int i = 0; i < graph[now].size(); i++) {
			int v = graph[now][i];
			
			result[v] = max(result[v], result[now] + times[v]);
			indegree[v] -= 1;
			
			// 진입차수가 0이라면
			if (indegree[v] == 0) q.push(v);
		}
	}
	
	for (int i = 1; i < n + 1; i++)
		cout << result[i] << '\n';
}

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	cin >> n;
	
	for (int i = 1; i < n + 1; i++) {
		int cost;
		cin >> cost;
		times[i] = cost;
		while (true) {
			int x;
			cin >> x;
			if (x == -1) break;
			
			// x -> i
			graph[x].push_back(i);
			indegree[i] += 1;
		}
	}
	
	topologySort();
	
	return 0;
}