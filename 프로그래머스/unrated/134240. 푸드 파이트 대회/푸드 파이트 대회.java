class Solution {
    public String solution(int[] food) {
        
        StringBuilder sb = new StringBuilder();

            for(int i = 0; i <food.length; i++){
                int div = food[i] / 2;
                for(int j = 0 ; j < div; j ++){
                    sb.append(i);
                }
                
            }
        String answer = sb.toString() + "0" + sb.reverse().toString();
                
        return answer;
    }
}