import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main{
   public static  void main (String[]args) throws NumberFormatException, IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        
        int[] arr = new int[n];
        
        for(int i=0; i<arr.length; i++){
            int a = Integer.parseInt(br.readLine());
            
            arr[i] = a;
        }
        Arrays.sort(arr);
        
        for(int b : arr) {
        	System.out.println(b);
        }
        
        
    }
}

