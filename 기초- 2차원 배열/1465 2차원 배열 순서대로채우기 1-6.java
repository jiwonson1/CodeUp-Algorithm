import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int[][] c = new int[a][b];
		int d=a*b;
		
		for (int i = 0; i < a; i++) { // i = 0,1
			for (int j = b-1; j >= 0; j--) { // j = 2,1,0
				c[i][j]=d;
				d--;
			}
			for (int j = 0; j < b; j++) { // j = 2,1,0
				System.out.print(c[i][j]+" ");
			}
			System.out.println();
		}
	}//main end 
}
