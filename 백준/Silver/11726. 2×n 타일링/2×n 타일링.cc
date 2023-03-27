#include <iostream>
#include <algorithm>
#define MAX 1001

using namespace std;

int dp[MAX] = {0, };
int n;

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    dp[1] = 1;
    dp[2] = 2;

    for (int i = 3; i < n + 1; i++)
        dp[i] = (dp[i-1] + dp[i-2]) % 10007;

    cout << dp[n] << '\n'; 
    return 0;
}