class Solution {
    public int solution(int[][] sizes) {
        int len = 0;
        int height = 0 ;
        for(int[] card: sizes){
            len = Math.max(len,Math.max(card[0],card[1]));
            height = Math.max(height,Math.min(card[0],card[1]));
            
        }
        int answer = len*height;
        return answer;
    }
}