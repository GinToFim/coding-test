#include <iostream>
using namespace std;
int n, k, temp, dp[10004], INF = 987654321;
int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	fill(dp, dp + 10004, INF);
	dp[0] = 0;
	cin >> n >> k;
	for (int i = 0; i < n; i++)
	{
		cin >> temp;
		for (int j = temp; j <= k; j++)
			dp[j] = min(dp[j], dp[j - temp] + 1);
	}
	if (dp[k] == INF) cout << -1 << "\n";
	else cout << dp[k] << "\n";
	return 0;
}