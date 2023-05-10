/*
아이디어 : 
알고리즘 : 크루스칼 (parent, edges, sort, cycle)
자료구조 : union-find
*/

#include <bits/stdc++.h>

#define MAX 1001

using namespace std;

int n, m;
int parent[MAX];
vector<pair<int, pair<int, int> > > edges;
int result = 0;

// find 연산 정의 (경로 압축)
int findParent(int x) {
	// 루트 노드가 아니라면, 루트 노드가 나올 때까지 재귀 호출
	if (parent[x] != x)
		parent[x] = findParent(parent[x]);
	return parent[x];
}

void unionParent(int a, int b) {
	a = findParent(a);
	b = findParent(b);
	
	if (a < b) parent[b] = a;
	else parent[a] = b;
}

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	cin >> n >> m;
	
	// 부모 테이블 초기화
	for (int i = 1; i < n + 1; i++) 
		parent[i] = i;
	
	// 간선 정보 입력
	for (int i = 0; i < m; i++) {
		int a, b, cost;
		cin >> a >> b >> cost;
		
		edges.push_back({cost, {a, b}});
	}
	
	// 간선 오름차순 정렬
	sort(edges.begin(), edges.end());
	
	for (int i = 0; i < m; i++) {
		int cost = edges[i].first;
		int a = edges[i].second.first;
		int b = edges[i].second.second;
		
		// 사이클이 생기지 않았다면
		if (findParent(a) != findParent(b)) {
			unionParent(a, b);
			result += cost;
		}
		
		
	}
	
	cout << result << '\n';
	return 0;
}