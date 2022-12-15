
import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = {};
        int idx = 0; 
        ArrayList<Integer> sumArr = new ArrayList<>();
        
        for(int i = 0 ; i <numbers.length-1; i ++){
            for (int j = i+1; j <numbers.length; j ++ ){
                int temp = numbers[i] + numbers[j];
                if(sumArr.indexOf(temp) <0) sumArr.add(temp);
                
                
            }
        }
        answer = new int[sumArr.size()];
        for(int num: sumArr){
            answer[idx++] = num;
        }
        Arrays.sort(answer);
        
        return answer;
    }
}