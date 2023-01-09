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
        StringTokenizer nSt = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(nSt.nextToken());
        int arr[] = new int[n];
        int sum[] = new int[n];
        long count = 0;

        StringTokenizer numSt = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++){
            arr[i] = Integer.parseInt(numSt.nextToken());
            if(i == 0){
                sum[i] = arr[i];
            }else{
                sum[i] = arr[i] + sum[i - 1];
            }
        }
        if(sum[n - 1] % 4 != 0){
            bw.write("0");
        } else if (sum[n - 1] == 0) {
            long zeroCnt = 0;
            for(int i = 0; i < n; i++){
                if(sum[i] == 0){
                    ++zeroCnt;
                }
            }
            String answer = Long.toString(((zeroCnt - 1) * (zeroCnt - 2) * (zeroCnt - 3)) / 6);
            bw.write(answer);
        } else{
            for(int j = 1; j <= n - 3; j++) {
                int sum1 = sum[j - 1];
                if(sum1 * 4 != sum[n - 1]){
                    continue;
                }
                for (int k = j + 1; k <= n - 2; k++) {
                    int sum2 = sum[k - 1] - sum[j - 1];
                    if(sum2 * 4 != sum[n - 1]){
                        continue;
                    }
                    for (int l = k + 1; l <= n - 1; l++) {
                        int sum3 = sum[l - 1] - sum[k - 1];
                        int sum4 = sum[n - 1] - sum[l - 1];
                        if (sum1 == sum2 && sum2 == sum3 && sum3 == sum4) {
                            ++count;
                        }

                    }
                }
            }
            String answer = Long.toString(count);
            bw.write(answer);
        }
        bw.newLine();
        bw.flush();
        bw.close();
    }
}