// 아이디어: 정렬
import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Arrays.sort(participant);
        Arrays.sort(completion);
        
        for (int i = 0; i < completion.length; i++) {
            // 현재 명단이 다르다면
            if (!participant[i].equals(completion[i])) {
                return participant[i];
            } 
        }
        
        return participant[participant.length - 1];
    }
}