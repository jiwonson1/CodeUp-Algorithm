import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		//StringTokenizer st = new StringTokenizer(br.readLine(), " "); 
		
		int n = Integer.parseInt(br.readLine());
		
		int c=n;
		
		//stringTokenizer 
		
		int [][] b = new int[n][n]; //2차원 배열 세팅
		
			for(int i=0; i<b.length; i++) {
				for(int j=0; j<b.length; j++) {
					b[i][j]+=c;
					System.out.print(b[i][j]+ " ");
					c+=n;
				
				}
				c=n;
				c-=i+1;
				System.out.println();
			}
}
}
