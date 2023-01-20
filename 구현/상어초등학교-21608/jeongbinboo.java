import java.io.*;
import java.util.*;
import java.lang.*;
public class jeongbinboo
{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer nSt = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(nSt.nextToken());
        int stuArr[][] = new int[n * n][5];
        int seatArr[][] = new int[n][n];
        int seatInfo[] = {0, 0, 0, 0, 0};
        int preference = 0;
        HashMap<Integer, Integer[]> stuMap = new HashMap<Integer, Integer[]>();

        for (int i = 0; i < n * n; i++) {
            Integer preferArr[] = {0, 0, 0, 0};
            StringTokenizer stuSt = new StringTokenizer(br.readLine());
            int stuNum = Integer.parseInt(stuSt.nextToken());
            stuArr[i][0] = stuNum;
            for (int j = 0; j < 4; j++) {
                stuArr[i][j + 1] = Integer.parseInt(stuSt.nextToken());
                preferArr[j] = stuArr[i][j + 1];
            }
            stuMap.put(stuNum, preferArr);
        }

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                seatArr[i][j] = 0;
            }
        }
        for (int i = 0; i < n * n; i++) {
            seatInfo[0] = 0;
            seatInfo[1] = 0;
            seatInfo[2] = 0;
            seatInfo[3] = 0;
            seatInfo[4] = 0;
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++){
                    if(seatArr[j][k] != 0){
                        continue;
                    }
                    int up = -1;
                    int down = -1;
                    int left = -1;
                    int right = -1;
                    int preferCount = 0;
                    int emptyCount = 0;

                    if(j != 0) {
                        up = seatArr[j - 1][k];
                    }
                    if(j != n - 1){
                        down = seatArr[j + 1][k];
                    }
                    if(k != 0){
                        left = seatArr[j][k - 1];
                    }
                    if(k != n - 1){
                        right = seatArr[j][k + 1];
                    }
                    if(up == stuArr[i][1] || up == stuArr[i][2] || up == stuArr[i][3] || up == stuArr[i][4]){
                        ++preferCount;

                    }
                    if(down == stuArr[i][1] || down == stuArr[i][2] || down == stuArr[i][3] || down == stuArr[i][4]){
                        ++preferCount;

                    }
                    if(left == stuArr[i][1] || left == stuArr[i][2] || left == stuArr[i][3] || left == stuArr[i][4]){
                        ++preferCount;

                    }
                    if(right == stuArr[i][1] || right == stuArr[i][2] || right == stuArr[i][3] || right == stuArr[i][4]){
                        ++preferCount;

                    }
                    if(up == 0){
                        ++emptyCount;
                    }
                    if(down == 0){
                        ++emptyCount;
                    }
                    if(left == 0){
                        ++emptyCount;
                    }
                    if(right == 0){
                        ++emptyCount;
                    }
                    if(preferCount > seatInfo[1]){
                        seatInfo[0] = stuArr[i][0];
                        seatInfo[1] = preferCount;
                        seatInfo[2] = emptyCount;
                        seatInfo[3] = j;
                        seatInfo[4] = k;
                    } else if (preferCount == seatInfo[1] && emptyCount > seatInfo[2]) {
                        seatInfo[0] = stuArr[i][0];
                        seatInfo[1] = preferCount;
                        seatInfo[2] = emptyCount;
                        seatInfo[3] = j;
                        seatInfo[4] = k;
                    }
                }
            }
            seatArr[seatInfo[3]][seatInfo[4]] = seatInfo[0];
        }
        for(int i = 0; i< n; i++){
            for(int j = 0; j < n; j++){
                int up = 0;
                int down = 0;
                int left = 0;
                int right = 0;
                int count = 0;
                int key = seatArr[i][j];

                if(i != 0) {
                    up = seatArr[i - 1][j];
                }
                if(i != n - 1){
                    down = seatArr[i + 1][j];
                }
                if(j != 0){
                    left = seatArr[i][j - 1];
                }
                if(j != n - 1){
                    right = seatArr[i][j + 1];
                }
                for(int k = 0; k < 4; k++){
                    if(up == stuMap.get(key)[k] || down == stuMap.get(key)[k] || left == stuMap.get(key)[k] || right == stuMap.get(key)[k]){
                        ++count;
                    }
                }
                if(count != 0){
                    preference += Math.pow(10, count - 1);
                }
            }
        }
        bw.write(Integer.toString(preference));
        bw.newLine();
        bw.flush();
        bw.close();
    }
}
