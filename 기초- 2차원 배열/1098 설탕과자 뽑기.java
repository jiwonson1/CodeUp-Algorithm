import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int h = sc.nextInt(); //세로
        int w = sc.nextInt(); //가로
        int n = sc.nextInt(); //막대 개수
        
        
        int[][] arr = new int[h][w]; //바둑판
        
        for(int i =0; i< n; i++){
            
            int l = sc.nextInt(); //막대 길이
            int d = sc.nextInt(); //막대 방향
            int x = sc.nextInt() - 1; //방향(x좌표)
            int y = sc.nextInt() - 1; //방향(y좌표)
            
           
           for(int j=0; j<l; j++){
               if(d==0){
                    if(y-1+j < 100-h){
                        arr[x][y+j] = 1;
                    }
               }else{
                    if(x-1+j < 100-w){
                        arr[x+j][y] = 1;
                    }
               }
             
           }
            
        }
        
        for (int a = 0; a < h; a++) {
			for (int b = 0; b < w; b++) {
				System.out.printf("%d ", arr[a][b]);
			}
			System.out.println();
		}
    }
}
