class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        int sm = a;
        int big = b;
         if (b<a){
             sm = b;
             big = a;
         }
        for(int i=sm; i<big+1;i ++){
            answer += i;
        }
        return answer;
    }
}