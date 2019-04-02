import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Main {

	public static void main(String[] args) {
				
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			try {
				int N = Integer.parseInt(br.readLine());
				List<String> line = Arrays.asList(br.readLine().split("\\s"));
				List<Long> data = line.stream().map(d -> Long.parseLong(d)).collect(Collectors.toList());
				
				System.out.printf("%d %d %d\n", 
						data.stream().min((a,b)-> a.compareTo(b)).get(),
						data.stream().max((a,b)-> a.compareTo(b)).get(),
						data.stream().mapToLong(d -> d).sum());
			}catch(IOException e) {
				e.printStackTrace();
			}
			
	}
}
