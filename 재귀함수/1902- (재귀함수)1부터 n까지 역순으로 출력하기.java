import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
static void f(int n) {
		if(n==0) 
				return;
		System.out.println(n); 
				f(n-1);    
	}
	public static void main (String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int b = Integer.parseInt(br.readLine());
		f(b);
	}
	
}
