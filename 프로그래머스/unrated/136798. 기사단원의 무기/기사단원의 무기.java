class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        for(int i = 1; i < number+1; i ++){
            int result =getNum(i);
            if (result <= limit) {
                answer += result;
            }
            else {
                answer += power;
            }
        }
        return answer;
    }
    
    static int getNum(int n){
        int cnt = 0 ; 
        for (int i=1; i*i <= n; i ++ ){
            if (n%i == 0 ){
                cnt ++;
                if (i*i < n) cnt++;
            }
        }
        return cnt;
    }
}