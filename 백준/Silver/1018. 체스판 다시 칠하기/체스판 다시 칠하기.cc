/*
아이디어 : 1. 원래 맞는 8x8 배열 만들어서 서로 비교하기 (맨 위쪽이 검은색 or 흰색)
          2. 입력받은 배열에 대해서 움직이면서 비교하기
알고리즘 : brute force => 50 X 50 X 2 = 5000
*/

#include <bits/stdc++.h>

using namespace std;

string wb[8] = {
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
};

string bw[8] = {
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"
};

int n, m;
vector<string> board;

int wb_cnt(int x, int y) {
    int cnt = 0;
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++)
            if (board[x+i][y+j] != wb[i][j])
                cnt++;
    }
    return cnt;
}

int bw_cnt(int x, int y){
    int cnt = 0;
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++)
            if (board[x+i][y+j] != bw[i][j])
                cnt++;
    }
    return cnt;
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    cin >> n >> m;
    
    // board 입력받기
    for (int i = 0; i < n; i++) {
        string row;
        cin >> row;
        board.push_back(row);
    }
    
    int result = 1e7;
    
    for (int i = 0; i <= n-8; i++) {
        for (int j = 0; j <= m-8; j++) {
            int tmp = min(wb_cnt(i, j), bw_cnt(i, j));
            result = min(result, tmp);
        }
    }
    
    cout << result << '\n';
    
    return 0;
}