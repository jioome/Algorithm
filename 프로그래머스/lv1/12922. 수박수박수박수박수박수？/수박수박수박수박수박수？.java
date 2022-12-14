class Solution {
    public String solution(int n) {

        char[] water = new char[n];

        for(int i =0 ; i<n; i++){
            if(i%2 == 0) water[i] = '수';
            else water[i]='박';
        }
        String answer = String.valueOf(water);
        return answer;
    }
}