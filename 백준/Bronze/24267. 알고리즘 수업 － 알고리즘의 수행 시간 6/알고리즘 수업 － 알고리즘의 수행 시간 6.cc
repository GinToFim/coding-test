#include <iostream>

using namespace std;

long long n;

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;

    cout << n * (n - 1) * (n - 2) / 6 << '\n' << 3 << '\n';
    return 0;
} 