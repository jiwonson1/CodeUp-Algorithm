import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[][] arr = new int[100][100];
		for(int i = 0; i < n; i++) {
			int k = sc.nextInt();
			for(int j = 0; j < i+1; j++) {
				arr[i][j] = k;
				if(j >= 1) {
					arr[i][j] = arr[i][j-1] - arr[i-1][j-1];
				}
			}
		}
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < i+1; j++) {
				System.out.printf("%d ", arr[i][j]);
			}
			System.out.println("");
		}
	}
}


