#include <bits/stdc++.h>

#define INF 1e9
#define MAX 801

using namespace std;

int n, e;
int v1, v2, res = INF;
int sToV1, sToV2, V1ToV2, V1ToN, V2ToN;
vector<pair<int, int> > v[MAX]; // v[a] = (b,c) : a에서 b까지 c의 거리로 이동 가능
int dist_table[MAX];

void dijk(int start)
{
	for (int i = 0; i <= n; i++) dist_table[i] = INF;
	dist_table[start] = 0;
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;
	q.push({ 0,start }); // 현재까지 거리, 현재 위치
	while (!q.empty()) {
		int cur = q.top().second;
		int curDist = q.top().first;
		q.pop();
		for (int i = 0; i < v[cur].size(); i++) {
			int next = v[cur][i].first;
			int nextDist = v[cur][i].second;
			if (dist_table[next] > curDist + nextDist) {
				dist_table[next] = curDist + nextDist;
				q.push({ dist_table[next],next });
			}
		}
	}
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
	cin >> n >> e;
	for (int i = 0; i < e; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		v[a].push_back({ b,c });
		v[b].push_back({ a,c });
	}
    
	cin >> v1 >> v2;

	dijk(1);
	sToV1 = dist_table[v1];
	sToV2 = dist_table[v2];

	dijk(v1);
	V1ToV2 = dist_table[v2];
	V1ToN = dist_table[n];

	dijk(v2);
	V2ToN = dist_table[n];


	res = min(res, sToV1 + V1ToV2 + V2ToN);
	res = min(res, sToV2 + V1ToV2 + V1ToN);
	if (V1ToV2 == INF || res == INF) cout << -1;
	else cout << res;
}