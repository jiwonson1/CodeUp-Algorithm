import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.StringTokenizer;
import java.util.TreeMap;


public class  Main {


	    public static void main(String args[]) throws NumberFormatException, IOException{
	        
	        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	        int n = Integer.parseInt(br.readLine());

	        TreeMap<Integer, String> map = new TreeMap<Integer, String>(Collections.reverseOrder());
	        
	        
	        for(int i=0; i<n; i++) {
	        	StringTokenizer s = new StringTokenizer(br.readLine(), " ");
	        	String b = s.nextToken();
	        	int a = Integer.parseInt(s.nextToken()); 
	        	map.put(a, b);
	        }
	        

	        int d = 1;
	        for(int a : map.keySet()) {
	        	d++;
	        	if(d==4) {
	        		System.out.println(map.get(a));
	        	}
	        }
}
}
