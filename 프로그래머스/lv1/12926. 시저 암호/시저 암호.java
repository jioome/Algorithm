class Solution {
    public String solution(String s, int n) {
        String answer = "";
        char[] ch = s.toCharArray();
        for(char c : ch){
            if(c == ' '){
                answer += c;
            }
            else if(c >='a' && c <='z'){
                answer += (char)('a' + (c+n-'a')%26);
            }
            else answer += (char)('A' + (c+n-'A')%26);
        }
        
        return answer;
    }
}