import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        
        Queue<Data> queue = new LinkedList<>();
        
        for (int i = 0; i < progresses.length; i++) {
            queue.offer(new Data(progresses[i], speeds[i]));
        }
        
        int day = 1;
        int cnt = 0;
        
        while(!queue.isEmpty()) {
            Data data = queue.peek();
            int p = data.getProgress();
            int s = data.getSpeed();
            
            if ((p + day * s) >= 100) {
                queue.poll();
                cnt += 1;
            } else {
                if (cnt > 0) {
                    answer.add(cnt);
                    cnt = 0;    
                }
               day += 1;     
            }
        } 
        if (cnt > 0) 
            answer.add(cnt);
        
        return answer.stream().mapToInt(x -> x).toArray();
    }
}

class Data {
    private int progress;
    private int speed;
    
    public Data(int progress, int speed) {
        this.progress = progress;
        this.speed = speed;
    }
    
    int getProgress() {
        return progress;
    }
    
    int getSpeed() {
        return speed;
    }
}