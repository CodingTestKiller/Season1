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
        int trainArr[] = new int[n];
        int arrived[] = new int[n];

        for(int i = 0; i < n; i++){
            trainArr[i] = 0;
        }
        for(int j = 0; j < m; j++){
            StringTokenizer instSt = new StringTokenizer(br.readLine());
            int mode = Integer.parseInt(instSt.nextToken());
            int i = Integer.parseInt(instSt.nextToken()) - 1;
            int x = 0;
            int isOn = 0;

            switch (mode){
                case 1:
                    x = Integer.parseInt(instSt.nextToken()) - 1;
                    isOn = trainArr[i] & (int)Math.pow(2, 19 - x);
                    if(isOn == 0){
                        trainArr[i] += Math.pow(2, 19 - x);
                    }
                    break;
                case 2:
                    x = Integer.parseInt(instSt.nextToken()) - 1;
                    isOn = trainArr[i] & (int)Math.pow(2, 19 - x);
                    if(isOn != 0){
                        trainArr[i] -= Math.pow(2, 19 - x);
                    }
                    break;
                case 3:
                    trainArr[i] = trainArr[i] >> 1;
                    break;
                case 4:
                    trainArr[i] = trainArr[i] << 1;
                    if(trainArr[i] > (Math.pow(2, 20) - 1)){
                        trainArr[i] -= Math.pow(2, 20);
                    }
                    break;
            }
        }
        arrived[0] = trainArr[0];
        for(int i = 1; i < n; i++){
            flag = 0;
            for(int j = 0; j < count; j++){
                if(arrived[j] == trainArr[i]){
                    flag = 1;
                    break;
                }
            }
            if(flag == 0){
                arrived[count] = trainArr[i];
                ++count;
            }
        }

        bw.write(Integer.toString(count));
        bw.newLine();
        bw.flush();
        bw.close();
    }
}
