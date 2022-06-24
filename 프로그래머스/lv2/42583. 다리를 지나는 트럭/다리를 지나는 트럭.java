import java.util.*;
class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        // 큐 초기화 
        Queue<Integer> q = new LinkedList<>();
        int max = 0;
        for(int w : truck_weights){
            while(true){
                if(q.isEmpty()){
                    q.offer(w);
                    max+=w;
                    // 시간 1초 쁠러스 
                    answer ++;
                    break;
                    //트럭이 다리를 다 지났으면 빼준다.
                }else if (q.size() == bridge_length){
                    max-=q.poll();
                }else{
                    // q가 비어있지 않고 무게가 초과될 때 0을 넣는다. 
                    if(max+w > weight){
                        q.offer(0);
                        answer ++;
                    }else{
                        q.offer(w);
                        max+= w;
                        answer ++;
                        break;
                    }
                }
            }
        }
        return answer+bridge_length;

    }
} 