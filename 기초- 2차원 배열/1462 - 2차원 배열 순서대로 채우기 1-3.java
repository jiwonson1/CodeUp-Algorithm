import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int[][] b = new int[a][a];
		int c=1;
		for (int i = 0; i < b.length; i++) {
			for (int j = 0; j < b.length; j++) {
				b[i][j]+=c;
				System.out.print(b[i][j]+" ");
				c+=a;
			}
			c=i+2;
			System.out.println();
		}
	}//main end 
}
