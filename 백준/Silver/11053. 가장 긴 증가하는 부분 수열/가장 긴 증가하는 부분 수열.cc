#include <iostream>
#include <algorithm>

using namespace std;

int n;
int arr[1001] = {0,};
int dp[1001] = {0, };

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        arr[i] = x;
        dp[i] = 1; // dp 테이블 초기화
    }

    int result = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (arr[i] > arr[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        result = max(dp[i], result);
    }
    cout << result << '\n';
    return 0;
}