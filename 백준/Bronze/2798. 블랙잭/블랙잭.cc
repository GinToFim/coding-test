/*
# 아이디어 :
# 알고리즘 : 브루트포스
*/

#include <bits/stdc++.h>

using namespace std;

int n, m;
vector<int> vec;

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    cin >> n >> m;
    
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        vec.push_back(x);
    }
    
    int result = 0;
    
    for (int i = 0; i < n-2; i++) {
        for (int j = i + 1; j < n - 1; j++) {
            for (int k = j + 1; k < n; k++) {
                int hap = vec[i] + vec[j] + vec[k];
                if (hap <= m)
                    result = max(result, hap);
            }
        }
    }
    
    cout << result << '\n';
    
    return 0;
}