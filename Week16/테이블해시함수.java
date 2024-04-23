import java.util.*;

class Solution {
    public int solution(int[][] data, int col, int row_begin, int row_end) {
        Arrays.sort(data, (e1, e2)-> {
            if (e1[col-1] != e2[col-1]){
                return Integer.compare(e1[col-1], e2[col-1]);
            }else{
                return Integer.compare(e2[0], e1[0]);
            }
        });
        int before = 0;
        for(int number: data[row_begin-1]){
            before += number % row_begin;
        }
        
        for(int idx = row_begin; idx < row_end; idx++){
            int sum = 0;
            for(int number: data[idx]){
                sum += number % (idx+1);
            }
            before ^= sum;
        }
        
        return before;
    }
}