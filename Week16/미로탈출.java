import java.util.Queue;
import java.util.LinkedList;

class Solution {
    static int lever_x;
    static int lever_y;
    static int n;
    static int m;
    static int[][] dxdy = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    public int solution(String[] maps) {
        n = maps.length;
        m = maps[0].length();
        for(int i = 0; i<n; i++){
            for(int j = 0; j<m; j++){
                if(maps[i].charAt(j) == 'L'){
                    lever_x = i;
                    lever_y = j;
                }
            }
        }
        int toStart = bfs(maps, 'S');
        int toEnd = bfs(maps, 'E');
        if(toStart == -1 || toEnd == -1){
            return -1;
        }else{
            return toStart+toEnd;
        }
        
    }
    
    public int bfs(String[] maps, char target_char) {
        Queue<int[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[n][m];
        visited[lever_x][lever_y] = true;
        queue.add(new int[] {0, lever_x, lever_y});
        while(!(queue.isEmpty())){
            int[] cur = queue.poll();
            
            for(int d = 0; d<4; d++){
                int next_x = cur[1] + dxdy[d][0];
                int next_y = cur[2] + dxdy[d][1];
                if(next_x < 0 || next_x >= n || next_y < 0 || next_y >= m) continue;
                if (maps[next_x].charAt(next_y) != 'X' && visited[next_x][next_y] == false){
                    if(maps[next_x].charAt(next_y) == target_char){
                        return cur[0] + 1;
                    }
                    visited[next_x][next_y] = true;
                    queue.add(new int[] {cur[0] + 1, next_x, next_y});
                }
            }
        }
        return -1;
        
    }
}