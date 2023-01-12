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
        String nm = br.readLine();
        StringTokenizer nmSt = new StringTokenizer(nm);
        int n = Integer.parseInt(nmSt.nextToken());
        int m = Integer.parseInt(nmSt.nextToken());
        int[][] sum = new int[n][n];
        int[] res = new int[m];

        for (int i = 0; i < n; i++){
            String arrData = br.readLine();
            StringTokenizer arrDataSt = new StringTokenizer(arrData);
            for (int j = 0; j < n; j++){
                int arrNum = Integer.parseInt(arrDataSt.nextToken());
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
                sum[i][j] = arrNum + src1 + src2 - src3;
            }
        }

        for (int i = 0; i < m; i++){
            String xy = br.readLine();
            StringTokenizer xySt = new StringTokenizer(xy);
            int x1 = Integer.parseInt(xySt.nextToken()) - 1;
            int y1 = Integer.parseInt(xySt.nextToken()) - 1;
            int x2 = Integer.parseInt(xySt.nextToken()) - 1;
            int y2 = Integer.parseInt(xySt.nextToken()) - 1;

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
            res[i] = sum[x2][y2] - src1 - src2 + src3;
            System.out.println(res[i]);
        }

    }
}