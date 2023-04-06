#include <iostream>

using namespace std;

string a, b;

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> a >> b;

    int lenA = a.length();
    int lenB = b.length();

    // 1. 무조건 A 자릿수를 크게 만들기
    if (lenB > lenA) {
        swap(a, b);
        swap(lenA, lenB);
    }

    // 2. 자릿수가 다르다면 맞추기 (1234, 32 -> 1232, 0032)
    string tmp = "";
    if (lenA > lenB) {
        for (int i = 0; i < (lenA - lenB); i++)
            tmp += "0";
    }
    b = tmp + b;

    // 3. 뒷자리부터 하나씩 result에 추가
    string result = "";
    int carry = 0; // 올림수
    int x, y, digit; // 자릿수

    for (int i = lenA-1; i >= 0; i--) {
        x = a[i] - '0';
        y = b[i] - '0';
        digit = x + y;

        if (carry == 1) {
            digit++;
            carry = 0;
        }
        if (digit > 9) //  올림하는 경우
            carry = 1;

        result += digit%10 + '0';
    }

    // 4. 마지막으로 추가되는 한 자리 ex) 23 + 95 = (1)18
    if (carry == 1)
        result += "1";

    // 5. 맨 뒤부터 거꾸로 출력
    for (int i = result.length() - 1; i >= 0; i--) {
        cout << result[i];
    }
    return 0;
}