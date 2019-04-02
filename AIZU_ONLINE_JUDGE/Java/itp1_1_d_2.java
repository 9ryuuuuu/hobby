import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		try {
			int S = Integer.parseInt(br.readLine());
			System.out.printf("%d:%d:%d\n", S/(60*60),(S%(60*60))/60,S%60);
			
		}catch(IOException e) {
			e.printStackTrace();
		}
	}

}
