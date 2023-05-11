/*
아이디어 :
알고리즘 : 브루트 포스
*/

#include <bits/stdc++.h>

using namespace std;

int n;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	cin >> n;
	
	int num = 665;
	int cnt = 0;
	
	while (cnt < n) {
		num++;
		int tmp = num;
		
		while (tmp >= 666) {
			if (tmp % 1000 == 666) {
				cnt++;
				break;
			}
			tmp /= 10;
		}
	}
	
	cout << num << '\n';
	
	return 0;
}