import java.util.Scanner;
import java.util.*;

class Main {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        String n = scan.next();
        
        int sum = 0;
        
        //n의 글자 수 만큼 배열을 생성한다.
        char[] num = new char[n.length()];
        
        //3의 배수 구하는 공식
        for(int i=0; i<num.length; i++){
            num[i] = n.charAt(i);
            sum+=num[i];
        }
        
        //3으로 나눠지면 3의 배수
        if(sum % 3 == 0){
            System.out.print("1");
        }else{
            System.out.print("0");
        }
        
        
    }
    
}
