#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<string> strlist) {
    vector<int> answer;
    
    for (int i = 0; i < strlist.size(); i++){
        answer.push_back(strlist[i].size());
    }
    return answer;
}