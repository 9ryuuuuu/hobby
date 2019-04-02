import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;

public class Main {

	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int cnt[][][] = new int[5][4][11];
		for(int i=1;i<5;i++) 
			for(int j=1;j<4;j++) 
				for(int k =1;k<11;k++) 
					cnt[i][j][k]=0;
		
		try {
			int N = Integer.parseInt(br.readLine()); 
			String tmp;
			while((tmp = br.readLine()) != null) {
				List<String> line = Arrays.asList(tmp.split("\\s"));
				int b = Integer.parseInt(line.get(0));
				int f = Integer.parseInt(line.get(1));
				int r = Integer.parseInt(line.get(2));
				int v = Integer.parseInt(line.get(3));
				cnt[b][f][r] += v;
				
			}
			br.close();
		}catch(IOException e) {
			e.printStackTrace();
		}

		for(int i=1;i<5;i++) { 
			for(int j=1;j<4;j++) { 
				for(int k =1;k<11;k++) { 
					System.out.printf(" %d", cnt[i][j][k]);
				}
				System.out.print("\n");
			}
			if(i != 4) System.out.print("####################\n");			
		}
					
	}
}
