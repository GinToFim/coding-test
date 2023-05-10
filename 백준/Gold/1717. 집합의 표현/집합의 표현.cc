/*
알고리즘 : union find (parent)
*/

#include <bits/stdc++.h>

#define MAX 1000001

using namespace std;

// 노드의 개수, 간선의 개수
int n, m;
int parent[MAX];

int findParent(int x) {
	// 루트 노드가 아니라면, 루트 노드일 때까지 재귀 호출
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
	
	// 연산 확인
	for (int i = 0; i < m; i++) {
		int op, a, b;
		cin >> op >> a >> b;
		
		// 합집합 수행
		if (!op) unionParent(a, b);
		else {
			a = findParent(a);
			b = findParent(b);
			if (a == b) cout << "YES" << '\n';
			else cout << "NO" << '\n';
		}
	}
	
	return 0;
}