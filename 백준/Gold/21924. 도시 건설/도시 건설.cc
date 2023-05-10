/*
아이디어 : root 노드 체크(만약 root 노드가 1이 아니라면 모든 도시 연결 x)
알고리즘 : 크루스칼 (parent, )
자료구조 : union-find
*/

#include <bits/stdc++.h>

#define MAX 100001

using namespace std;

int n, m;
int parent[MAX];
vector<pair<int, pair<int, int> > > edges;
long long int result = 0;
long long int total = 0; // 총 비용

// find 연산 수행 (경로 압축 기법)
int findParent(int x) {
	if (parent[x] != x)
		parent[x] = findParent(parent[x]);
	return parent[x];
}

// union 연산 수행
void unionParent(int a, int b) {
	a = findParent(a);
	b = findParent(b);
	
	if (a < b) parent[b] = a;
	else parent[a] = b;
}

bool isAllConnected() {
	for (int i = 2; i < n + 1; i++) {
		if (findParent(1) != findParent(i)) {
			return false;
		}
	}
	return true;
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
		total += cost;
		edges.push_back({cost, {a, b}});
	}
	
	// 간선 오름차순
	sort(edges.begin(), edges.end());
	
	for (int i = 0; i < m; i++) {
		int cost = edges[i].first;
		int a = edges[i].second.first;
		int b = edges[i].second.second;
		
		// 사이클이 발생하지 않았다면
		if (findParent(a) != findParent(b)) {
			unionParent(a, b);
			result += cost;
		}
	}
	
	// 절약 비용 확인
	total -= result;
	
	if (isAllConnected()) 
		cout << total << '\n';
	else 
		cout << -1 << '\n';
	
	return 0;
}