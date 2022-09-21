import java.util.Arrays;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        
        Arrays.sort(lost);
        Arrays.sort(reserve);
            
        for (int i=0; i<lost.length; i++) {
            for (int j=0; j<reserve.length; j++) {
                if (reserve[j] == lost[i]) {
                    lost[i] = -1;
                    reserve[j] = -1;
                    answer++;
                    break;
                }
            }
        }
        for (int i=0; i<lost.length; i++) {
            for (int j=0; j<reserve.length; j++) {
                if (reserve[j]-1 == lost[i] || reserve[j]+1 == lost[i]) {
                    answer++;
                    reserve[j] = -1;
                    break;
                }
            }
        }
        
        return n - lost.length + answer;
    }
}