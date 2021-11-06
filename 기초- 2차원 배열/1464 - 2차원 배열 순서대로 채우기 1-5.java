import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int[][] c = new int[a][b];
		int d=a*b;
		for (int i = 0; i < a; i++) {
			for (int j = 0; j < b; j++) {
				c[i][j]=d;
				System.out.print(c[i][j] +" ");
				d--;
			}
			System.out.println();
		}
	}//main end 
}
