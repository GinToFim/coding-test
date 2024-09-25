import java.util.*;

class Solution {
    public int solution(int[] nums) {
        
        HashSet<Integer> hashSet = new HashSet<>();
        
        for(int num: nums) {
            hashSet.add(num);
        }
        
        int minValue = Math.min(nums.length / 2, hashSet.size());
        
        return minValue;
    }
}