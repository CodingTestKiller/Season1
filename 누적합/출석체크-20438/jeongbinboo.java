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
        int k = Integer.parseInt(attendanceDataSt.nextToken());
        int q = Integer.parseInt(attendanceDataSt.nextToken());
        int m = Integer.parseInt(attendanceDataSt.nextToken());
        int stu[] = new int[n + 3];
        int sum[] = new int[n + 3];
        int sleepingStu[] = new int[k];
        int gettingCodeStu[] = new int[q];

        for(int i = 0; i < n + 3; i++){
            stu[i] = 0;
        }
        StringTokenizer sleepingSt = new StringTokenizer(br.readLine());
        for(int i = 0; i < k; i++){
            int sleepingNum = Integer.parseInt(sleepingSt.nextToken());
            stu[sleepingNum] = -1;
        }
        StringTokenizer gettingCodeSt = new StringTokenizer(br.readLine());
        for(int i = 0; i < q; i++){
            int j = 1;
            int gettingCodeNum = Integer.parseInt(gettingCodeSt.nextToken());
            while(gettingCodeNum * j <= n + 2){
                if(stu[gettingCodeNum * j] == -1){
                    if(j == 1){
                        break;
                    }
                    j++;
                    continue;
                }
                stu[gettingCodeNum * j] = 1;
                j++;
            }
        }
        sum[0] = 0;
        for(int i = 1; i < n + 3; i++){
            if(stu[i] == -1){
                stu[i] = 0;
            }
            sum[i] = sum[i - 1] + stu[i];
        }

        for(int i = 0; i < m; i++){
            StringTokenizer numOfRangeSt = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(numOfRangeSt.nextToken());
            int end = Integer.parseInt(numOfRangeSt.nextToken());
            String result = Integer.toString((end - start + 1) - (sum[end] - sum[start - 1]));
            bw.write(result);
            bw.newLine();
            bw.flush();
        }
        bw.close();
    }
}