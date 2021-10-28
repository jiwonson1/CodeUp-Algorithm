import java.util.*;

public class Main{
    
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x = n*n;
        
        for(int i=1; i<x+1; i++){
    
            if(i%n == 0){
                System.out.println(i);
            }else{
                System.out.print(i+" ");
            }
    
        }
        
    }
    
}
