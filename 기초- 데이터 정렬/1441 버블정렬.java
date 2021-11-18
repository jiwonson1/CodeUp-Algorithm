import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);

    int a = scan.nextInt();

    int[] arr = new int[a];

    for(int i = 0; i < arr.length; i++){
      int b = scan.nextInt();

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


