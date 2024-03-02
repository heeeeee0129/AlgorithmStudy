package Week9;

import java.util.Arrays;

public class FriendsBlock {
    public static char[][] blockBoard;
    public static boolean[][] popFlag;
    public static int[][] move = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    int erase = 0;
    int height;
    int width;
    public int solution(int m, int n, String[] board) {
        height = m;
        width = n;
        blockBoard = new char[m][n];
        popFlag = new boolean[m][n];
        
        for(int i=0; i<m; i++) {
            for(int j=0; j<n; j++) {
                blockBoard[i][j] = board[i].charAt(j);
            }
        }
        while (pop()) {
            update();
            initialize();
        }
        
        return erase;
    }
    
    void update() {
        for(int i=0; i<popFlag.length; i++) {
            for(int j=0; j<popFlag[i].length; j++) {
                if (popFlag[i][j]) {
                    blockBoard[i][j] = '0';
                    erase++;
                }
            }
        }
    }
    
    void initialize() {
        for (int i=0; i<popFlag.length; i++) {
            Arrays.fill(popFlag[i], false);
        }
        
        for (int i=0; i<width; i++) {
            boolean stillBlank = true;
            while (stillBlank) {
                // 캐릭터 나올 때까지 빈칸 스킵
                int row = 0;
                while(row < height && blockBoard[row][i] == '0') row++;

                // 빈칸 나올 때까지 스킵
                int plus = 0;
                while (row + plus < height && blockBoard[row+plus][i] != '0') plus++;

                // 빈칸 없으면 다음 열
                if (row + plus == height) break;

                // 얼만큼 내려야 하는 지 카운트
                int popStart = row + plus;
                int popRange = 1;
                while (popStart + popRange < height && blockBoard[popStart + popRange][i] == '0') popRange++;
                // 밑에 있는 블록부터 내림
                for(int j=row + plus - 1; j >= row; j--) {
                    blockBoard[j + popRange][i] = blockBoard[j][i];
                    blockBoard[j][i] = '0';
                }
                
                stillBlank = false;
                //밑에서부터 검사했을 때 캐릭터 사이에 공백 있으면 다시
                for(int j=height-2; j>=0; j--) {
                    if (blockBoard[j][i] != '0' && blockBoard[j+1][i] == '0') {
                        stillBlank = true;
                        break;
                    }
                }
            }
            
        }
    }
    
    boolean pop() {
        boolean anyPop = false;
        for(int i=0; i<height-1; i++) {
            for(int j=0; j<width-1; j++) {
                if (blockBoard[i][j] == '0') continue;
                boolean allSame = true;
                char elem = blockBoard[i][j];
                for(int m=i; m<=i+1; m++) {
                    for(int n=j; n<=j+1; n++){
                        if (blockBoard[m][n] != elem) {
                            allSame = false;
                            break;
                        }
                    }
                }
                if (allSame) {
                    for(int m=i; m<=i+1; m++) {
                        for(int n=j; n<=j+1; n++){
                            popFlag[m][n] = true;
                            anyPop = true;
                        }
                    }
                }
            }
        }
        return anyPop;
    }
}
