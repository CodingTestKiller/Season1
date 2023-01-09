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
        for(int j = 1; j <= n - 3; j++){
            for(int k = j + 1; k <= n - 2; k++){
                for(int l = k + 1; l <= n - 1; l++){
                    int sum1 = sum[j - 1];
                    int sum2 = sum[k - 1] - sum[j - 1];
                    int sum3 = sum[l - 1] - sum[k - 1];
                    int sum4 = sum[n - 1] - sum[l - 1];
                    if(sum1 == sum2 && sum2 == sum3 && sum3 == sum4){
                        ++count;
                    }

                }
            }

        }
        String answer = Long.toString(count);
        bw.write(answer);
        bw.newLine();
        bw.flush();
        bw.close();
    }
}