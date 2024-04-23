import java.util.*;

class Solution {
    
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    
    
    public int[] solution(String[][] places) {
        int[] answer = new int[places.length];
        for(int k=0; k<places.length; k++){
            boolean flag = false;
            for(int i = 0; i<5; i++){
                for(int j = 0; j<5; j++){
                    if(places[k][i].charAt(j) == 'P'){
                        boolean[][] visited = new boolean[5][5];
                        Queue<int[]> queue = new ArrayDeque<>();
                        queue.add(new int[] {i, j, 0});
                        while(!(queue.isEmpty()) && flag == false){
                            int[] cur = queue.poll();
                            if(cur[2] == 2){
                                continue;
                            }
                            visited[cur[0]][cur[1]] = true;
                            for(int d = 0; d<4; d++){
                                int next_x = cur[0] + dx[d];
                                int next_y = cur[1] + dy[d];
                                if(next_x >= 0 && next_x < 5 && next_y>= 0 && next_y < 5 && visited[next_x][next_y] == false){
                                    if(places[k][next_x].charAt(next_y) == 'O'){
                                        queue.add(new int[] {next_x, next_y, cur[2] + 1});
                                    }
                                    else if(places[k][next_x].charAt(next_y) == 'P'){
                                        flag = true;
                                        break;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        
        if(flag == false){
            answer[k] = 1;
        }else{
            answer[k] = 0;
        }
        }
        return answer;
    }
}