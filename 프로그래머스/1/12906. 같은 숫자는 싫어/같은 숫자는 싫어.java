import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        Stack<Integer> answer = new Stack<>();
        
        answer.add(arr[0]);
        
        for (int i = 1; i < arr.length; i++) {
            if (answer.peek() == arr[i]) 
                continue;
            
            answer.add(arr[i]);
        }
        
        return answer.stream().mapToInt(x -> x).toArray();
    }
}