import java.util.*;
class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        // 오름차순 정렬 
        Arrays.sort(score);
        // 배열 만들기 
        int[] tScore = new int[score.length];
        
        // 역순으로 정렬 하기 
        for(int i=0; i < score.length; i++){
            tScore[i] = score[score.length-1-i];
        }
        
        int index = 0 ;
        // 배열에서 크기만큼 잘라서 계산 
        
        while(true) {
            // 뒤에 있는 인덱스 or 넘어갈 때는 그냥 멈춘다. 
            if(index >= tScore.length || index + m > tScore.length){
                break;
            }
            // 마지막 인덱스 * m
            answer += tScore[index + m -1] *m;
            // 인덱스 다음 상자 시작 
            index += m;
        }
        
        return answer;
    }
}