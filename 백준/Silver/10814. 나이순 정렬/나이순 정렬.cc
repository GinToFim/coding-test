#include <iostream>
#include <algorithm>

using namespace std;

struct Person {
    int age;
    string name;
};

int n;

bool compare(const Person& first, const Person& second) {
    return first.age < second.age;
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    Person p[100001];
    for (int i = 0; i < n; i++) {
        cin >> p[i].age >> p[i].name;
    }

    // stable_sort
    stable_sort(p, p + n, compare);

    for (int i = 0; i < n; i++) {
        cout << p[i].age << ' ' << p[i].name << '\n';
    }

    return 0;
}