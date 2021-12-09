import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;
import java.util.Arrays;
public class Main {
    
 static void f() throws NumberFormatException, IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int b = Integer.parseInt(br.readLine());
        //정렬전 배열
        Integer []arr = new Integer[b];
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        
        for(int i =0; i<b; i++) {
        	arr[i] = Integer.parseInt(st.nextToken()); // [40, 30, 10, 20] 4 3 1 2
        };
        
        //정렬후 배열
        Integer []arr2 = arr.clone();
        Arrays.sort(arr2);
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        
        for(int i=0; i<b; i++) {
        	map.put(arr2[i], i+1); // value에 위치가 있음 <10, 1>, <20, 2>, <30, 3>, <40, 4>
        };
        
        int answer = 0;
        //value로 key 찾기
        Set<Entry<Integer, Integer>> entrySet = map.entrySet();
        for(Entry<Integer, Integer> entry : entrySet) {
        	if(entry.getValue().equals(b)) {
        		//System.out.println(entry.getKey());
        		answer = entry.getKey();
        	}
        }
        int getIndex = Arrays.asList(arr).indexOf(answer);
		System.out.print(getIndex+1);
        
    }
    
    public static void main(String args[]) throws NumberFormatException, IOException{
        f();
    }
    
}
