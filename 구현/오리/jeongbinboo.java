import java.io.*;
import java.util.*;
import java.lang.*;
public class jeongbinboo
{
    public static int getCnt(int[] quackArr){
        int cnt = 0;
        for(int i = 0; i < 4; i++){
            cnt += quackArr[i];
        }
        return cnt;
    }

    public static void printException() throws IOException{
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write("-1");
        bw.flush();
        bw.close();
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int maxDuckCnt = 0;
        int quackArr[] = {0, 0, 0, 0};
        HashMap<String, Integer> quackMap = new HashMap<>(5);
        quackMap.put("q", 0);
        quackMap.put("u", 1);
        quackMap.put("a", 2);
        quackMap.put("c", 3);
        quackMap.put("k", 4);

        StringTokenizer quackSt = new StringTokenizer(br.readLine());
        String quack = quackSt.nextToken();
        for(int i = 0; i < quack.length(); i++){
            char quackChar = quack.charAt(i);
            if(!quackMap.containsKey(Character.toString(quackChar))){
                printException();
                bw.close();
                return;
            }
            int quackIndex = quackMap.get(Character.toString(quackChar));
            if(quackChar == 'q'){
                quackArr[0] += 1;
            } else if (quackChar == 'k') {
                int cnt = getCnt(quackArr);
                if(cnt > maxDuckCnt){
                    maxDuckCnt = cnt;
                }
                quackArr[3] -= 1;
            } else{
                if(quackArr[quackIndex - 1] == 0){
                    printException();
                    bw.close();
                    return;
                }
                quackArr[quackIndex - 1] -= 1;
                quackArr[quackIndex] += 1;
            }
        }
        int cnt = getCnt(quackArr);
        if(cnt != 0){
            printException();
            bw.close();
            return;
        }
        bw.write(Integer.toString(maxDuckCnt));
        bw.flush();
        bw.close();
    }
}
