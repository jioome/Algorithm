import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        // 배열 만들기 
        List<Integer> answ = new ArrayList<Integer>();
        // arr 반복문 
        for(int i=0; i<arr.length; i++){
            // 반복되지 않으면 추가 
            if(i!= arr.length-1 && arr[i] !=arr[i+1]) answ.add(arr[i]);
            // 맨 마지막이면 추가 
            if(i == arr.length -1)answ.add(arr[i]);
        }
            // 배열 만들기 
            int[] answer = new int[answ.size()];
            for(int j = 0 ; j<answ.size(); j++){
                answer[j] = answ.get(j);
            
        }
        
        

        return answer;
    }
}