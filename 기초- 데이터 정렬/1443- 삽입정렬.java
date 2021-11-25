import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class  Main {


	    public static void main(String args[]) throws NumberFormatException, IOException{
	        
	        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	        int a = Integer.parseInt(br.readLine());
	        
	        int[] arr = new int[a];

            for(int i = 0; i < arr.length; i++){
              int b = Integer.parseInt(br.readLine());

              arr[i] = b;
            }
        
            for(int i = arr.length-1; i > 0; i--){
              for(int j = 0; j < i; j++){
                if(arr[j] > arr[j + 1]){
                  int temp = arr[j];
                  arr[j] = arr[j +1];
                  arr[j + 1] = temp;
                }
              }
            }
        
            for(int i = 0; i < arr.length; i++){
              System.out.printf("%d\n", arr[i]);
            }
        
        	}
}

