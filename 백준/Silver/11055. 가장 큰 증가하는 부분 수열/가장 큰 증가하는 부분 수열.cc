#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n;
vector<int> v;
vector<int> dp;

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        v.push_back(x);
        dp.push_back(x); // dp 테이블 초기화
    }

    int result = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (v[i] > v[j]) {
                dp[i] = max(dp[i], dp[j] + v[i]);
            }
        }
        result = max(result, dp[i]);
    }

    cout << result << '\n';
    return 0;
}