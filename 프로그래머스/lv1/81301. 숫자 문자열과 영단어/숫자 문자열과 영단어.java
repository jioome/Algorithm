class Solution {
    public int solution(String s) {

        String[] number = {"zero","one","two","three","four","five","six","seven","eight","nine"};
        int index = 0 ;
        
        for(String num : number){
            if(s.contains(num)) s = s.replace(num,String.valueOf(index));
            index ++;
        }
        int answer = Integer.parseInt(s);
            
        
        return answer;
    }
}