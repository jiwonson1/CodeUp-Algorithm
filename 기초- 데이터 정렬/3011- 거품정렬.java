import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String args[]) throws NumberFormatException, IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		//데이터 개수
		int b = Integer.parseInt(br.readLine());
		//총 데이터가 들어갈 배열
		int []arr = new int[b];
		//데이터 교환 시 임시변수
		int temp = 0;
		//데이터 교환이 일어났는지 확인하는 변수
		boolean sortCheck = false;
		//정렬 단계를 저장할 변수
		int result = 0;
		
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		for(int i =0; i<arr.length; i++){
			arr[i] = Integer.parseInt(st.nextToken());
		}
		  for(int i = (arr.length -1); i>0; i--) {
			  for(int j = 0; j<i; j++){
				  if(arr[j] > arr[j+1]) { 
					  temp = arr[j];
					  arr[j] = arr[j+1]; 
					  arr[j+1] = temp; 
					  sortCheck = true; 
					  } 
				  }
			  if(sortCheck == true) { 
				  result++;
				  sortCheck = false;
			  }else {
				  break;
			  } 
		  }
		  System.out.println(result);
		
	};
}
