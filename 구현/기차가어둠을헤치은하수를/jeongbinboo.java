import java.io.*;
import java.util.*;
import java.lang.*;
public class jeongbinboo
{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer nmSt = new StringTokenizer(br.readLine());
        int count = 1;
        int flag = 0;

        int n = Integer.parseInt(nmSt.nextToken());
        int m = Integer.parseInt(nmSt.nextToken());
        char trainArr[][] = new char[n][20];
        StringBuilder seatArr[] = new StringBuilder[n];
        StringBuilder arrived[] = new StringBuilder[n];

        for(int i = 0; i < n; i++){
            for(int j = 0; j < 20; j++){
                trainArr[i][j] = 'X';
            }
        }
        for(int j = 0; j < m; j++){
            StringTokenizer instSt = new StringTokenizer(br.readLine());
            int mode = Integer.parseInt(instSt.nextToken());
            int i = Integer.parseInt(instSt.nextToken()) - 1;
            if(mode == 1){
                int x = Integer.parseInt(instSt.nextToken()) - 1;
                trainArr[i][x] = 'O';
            } else if(mode == 2) {
                int x = Integer.parseInt(instSt.nextToken()) - 1;
                trainArr[i][x] = 'X';
            } else if(mode == 3){
                for(int k = 19; k >= 1; k--){
                    trainArr[i][k] = trainArr[i][k - 1];
                }
                trainArr[i][0] = 'X';
            } else if (mode == 4) {
                for(int k = 0; k <= 18; k++){
                    trainArr[i][k] = trainArr[i][k + 1];
                }
                trainArr[i][19] = 'X';
            }
        }
        for(int i = 0; i < n; i++){
            StringBuilder seat = new StringBuilder();
            for(int j = 0; j < 20; j++){
                seat.append(trainArr[i][j]);
            }
            seatArr[i] = seat;
        }
        arrived[0] = seatArr[0];
        for(int i = 1; i < n; i++){
            flag = 0;
            for(int j = 0; j < count; j++){
                if(seatArr[i].toString().equals(arrived[j].toString())) {
                    flag = 1;
                    break;
                }
            }
            if(flag == 0){
                arrived[count] = seatArr[i];
                ++count;
            }
        }
        bw.write(Integer.toString(count));
        bw.newLine();
        bw.flush();
        bw.close();
    }
}

