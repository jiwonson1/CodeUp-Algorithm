import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
static void f(int n) {
		if(n==0) 
				return;
				f(n-1);    
				System.out.println(n); 
	}
	public static void main (String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int b = Integer.parseInt(br.readLine());
		f(b);
	}
}
