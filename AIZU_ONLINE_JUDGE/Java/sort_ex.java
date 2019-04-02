import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class Main {

	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		try {
			Integer N = Integer.parseInt(br.readLine());
			List<String> line = Arrays.asList( br.readLine().split("\\s"));
			List<Integer> data = line.stream().map(d -> Integer.parseInt(d)).collect(Collectors.toList());
			Collections.sort(data, Collections.reverseOrder());
			
			for(int i=0;i<data.size();i++) {
				System.out.printf("%d", data.get(i));
				if(i != data.size()-1) {
					System.out.print(" ");
				}
			}
			System.out.print("\n");

		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}
