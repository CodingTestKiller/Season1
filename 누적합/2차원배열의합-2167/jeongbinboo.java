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

        for(int i = 0; i < n; i++){
            StringTokenizer arrDataSt = new StringTokenizer(br.readLine());
            for(int j = 0; j < m; j++){
                int src1 = 0;
                int src2 = 0;
                int src3 = 0;
                if (i != 0){
                    src1 = sum[i - 1][j];
                }
                if (j != 0){
                    src2 = sum[i][j - 1];
                }
                if (i != 0 && j != 0){
                    src3 = sum[i - 1][j - 1];
                }
                arr[i][j] = Integer.parseInt(arrDataSt.nextToken());
                sum[i][j] = arr[i][j] + src1 + src2 - src3;
            }
        }
        StringTokenizer kSt = new StringTokenizer(br.readLine());
        int k = Integer.parseInt(kSt.nextToken());
        for(int p = 0; p < k; p++){
            StringTokenizer indexSt = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(indexSt.nextToken()) - 1;
            int j = Integer.parseInt(indexSt.nextToken()) - 1;
            int x = Integer.parseInt(indexSt.nextToken()) - 1;
            int y = Integer.parseInt(indexSt.nextToken()) - 1;
            int src1 = 0;
            int src2 = 0;
            int src3 = 0;
            if (i != 0){
                src1 = sum[i - 1][y];
            }
            if (j != 0){
                src2 = sum[x][j - 1];
            }
            if (i != 0 && j != 0){
                src3 = sum[i - 1][j - 1];
            }
            String result = Integer.toString(sum[x][y] - src1 - src2 + src3);
            bw.write(result);
            bw.newLine();
            bw.flush();
        }
        bw.close();
    }
}