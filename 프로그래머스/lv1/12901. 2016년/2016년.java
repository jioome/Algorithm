class Solution {
    public String solution(int a, int b) {
        String answer = "";
        String[] days = {"SUN","MON","TUE","WED","THU","FRI","SAT"};
        int[] months = {0,31,29,31,30,31,30,31,31,30,31,30};
        int total = 0 ; 
        for(int i = 0; i < a; i ++){
            total += months[i];
        }
        total += b ; 
        answer = days[(total+4)%7];
        

        return answer;
    }
}