import java.util.*;
class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 1; // 출력순서. 몇 번재로 출력되는가? 
        PriorityQueue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());
        //우선순위 내림차순 정렬하기 
        for (int priority : priorities){
            queue.offer(priority);
        }
        while(!queue.isEmpty()){
            for (int i = 0 ; i <priorities.length; i++){
                if (queue.peek() == priorities[i]){
                    if (i == location){
                        return answer;
                    }
                    answer ++;
                    queue.poll(); // 값을 찾았을 때만 큐에서 빼야함 ;; 
                }
            }
        }
        return answer;
    }
}