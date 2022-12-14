import java.util.*;
class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        Arrays.sort(d);
        for(int x : d){
            if(budget>=x) {
                answer ++;
                budget -= x;
            }
            
            
        }
        return answer;
    }
}