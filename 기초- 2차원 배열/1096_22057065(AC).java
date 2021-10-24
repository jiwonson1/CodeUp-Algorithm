import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[][] arr = new int[19][19];
        int n = scanner.nextInt();

        // 흰 돌의 수만큼 반복
        for (int i = 0; i < n; i++) {
            int whichx = scanner.nextInt(); // x위치를 받음
            int whichy = scanner.nextInt(); // y위치를 받음

			// x,y좌표를 2차원 배열에 표시
            for (int x = 0; x < arr.length; x++) {
                for (int y = 0; y < arr.length; y++) {
                    arr[whichx - 1][whichy - 1] = 1;
                }
            }
        }

		// 출력
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }


    }

}

