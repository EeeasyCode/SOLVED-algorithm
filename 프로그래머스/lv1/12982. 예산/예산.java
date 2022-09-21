import java.util.*;

class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        int all_sum = 0;
        int sum = 0;
        int count = 0;
        Arrays.sort(d);
        
        for (int i=0; i < d.length; i++) {
            if (sum <= budget) {
                sum += d[i];   
                count ++;
            }
            if (sum > budget) {
                sum -= d[i];
                count --;
                break;
            }
        }
        
        return count;
    }
}