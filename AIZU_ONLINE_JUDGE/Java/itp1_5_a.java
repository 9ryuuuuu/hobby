import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;

public class Main {

	public static void main(String[] args) {
		
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			try {
				while(true) {
					List<String> line =  Arrays.asList(br.readLine().split("\\s"));
					int a = Integer.parseInt(line.get(0)); 
					int b = Integer.parseInt(line.get(1));
					if((a==0)&&(b==0)) {
						break;
					}
					for(int i=0;i<a;i++) {
						for(int j=0;j<b;j++) {
							System.out.print("#");
						}
						System.out.print("\n");
					}
					System.out.print("\n");

				}
			}catch(IOException e) {
				e.printStackTrace();
			}
	}
}
