import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.Arrays;

public class Main{

public static void main(String args[]) throws NumberFormatException, IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int b = Integer.parseInt(br.readLine());
		
		int []arr = new int[b];
		
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		for(int i=0; i<arr.length; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		int []arr2 = arr.clone();
		
		Arrays.sort(arr); // 재정렬 했음 > 40, 50 ,60 
		//arr2는 재정렬 전 ->60 40 50
		
		Map<Integer, Integer> map = new HashMap<Integer, Integer>();
		
		for(int i=0; i<b; i++) {
			map.put(arr[i], i);
		}
		// <40, 0>, <50, 1> , <60, 2> 형태로 들어가 있음.
		
		for(int num : arr2) {
			System.out.print(map.get(num)+" ");
		}
		//출력한다 -> arr2 처음에 담았던 숫자를 for문 돌려서 map에 있는 걸 꺼냄.
		// key , value로 들어가있음 꺼내야할 것은 value. 
		br.close();
		
	}
	
}
