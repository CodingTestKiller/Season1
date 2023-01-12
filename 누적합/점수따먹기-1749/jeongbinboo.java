import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;

public class jeongbinboo
{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer attendanceDataSt = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(attendanceDataSt.nextToken());
        int m = Integer.parseInt(attendanceDataSt.nextToken());
        int arr[][] = new int[n][m];
        int sum[][] = new int[n][m];
        int max = 0;
        int result = 0;

        for(int i = 0; i < n; i++){
            StringTokenizer arrDataSt = new StringTokenizer(br.readLine());
            for(int j = 0; j < m; j++){
                int src1 = 0;
                int src2 = 0;
                int src3 = 0;
                if(i != 0){
                    src1 = sum[i - 1][j];
                }
                if(j != 0){
                    src2 = sum[i][j - 1];
                }
                if(i != 0 && j != 0){
                    src3 = sum[i - 1][j - 1];
                }
                arr[i][j] = Integer.parseInt(arrDataSt.nextToken());
                sum[i][j] = arr[i][j] + src1 + src2 - src3;
            }
        }
        for(int x1 = 0; x1 < n; x1++){
            for(int y1 = 0; y1 < m; y1++){
                for(int x2 = x1; x2 < n; x2++){
                    for(int y2 = y1; y2 < m; y2++){
                        int src1 = 0;
                        int src2 = 0;
                        int src3 = 0;
                        if(x1 != 0){
                            src1 = sum[x1 - 1][y2];
                        }
                        if(y1 != 0){
                            src2 = sum[x2][y1 - 1];
                        }
                        if(x1 != 0 && y1 != 0){
                            src3 = sum[x1 - 1][y1 - 1];
                        }
                        result = sum[x2][y2] - src1 - src2 + src3;
                        if(x1 == 0 && y1 == 0 && x2 == 0 && y2 == 0){
                            max = result;
                        }else{
                            if(result > max){
                                max = result;
                            }
                        }
                    }
                }
            }
        }
        String answer = Integer.toString(max);
        bw.write(answer);
        bw.newLine();
        bw.flush();
        bw.close();
    }
}