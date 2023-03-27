#include <iostream>
#include <algorithm>
#define MAX 1000001

using namespace std;

// dp 테이블 선언
int dp[MAX] = {0, };
int x;

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> x;
    dp[2] = 1;

    for (int i = 3; i < x + 1; i++) {
        dp[i] = dp[i-1] + 1;

        // 2로 나눌 수 있다면
        if (i % 2 == 0) {
            dp[i] = min(dp[i], dp[i/2] + 1);
        }

        if (i % 3 == 0) {
            dp[i] = min(dp[i], dp[i/3] + 1);
        }
    }

    cout << dp[x] << '\n';
    return 0;
}