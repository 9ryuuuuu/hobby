import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {

	public static void main(String[] args) {
//		String baseUrl = "C:\\Users\\kuriyama.akira\\git-repository\\hobby\\AIZU_ONLINE_JUDGE\\Java\\";
//		String filePath = baseUrl +  "inp_itp_1_6_b.txt";
//		FileInputStream fis = null; 
//		try { 
//			fis = new FileInputStream(new File(filePath));
//		}catch(FileNotFoundException e){
//			e.printStackTrace();
//		}
//		BufferedReader br = new BufferedReader(new InputStreamReader(fis));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		boolean card[][] = new boolean[4][14];
		for(int i=0;i<4;i++) {
			for(int j=1;j<14;j++) {
				card[i][j] = false;
			}
		}
		
		Map<String, Integer> designInt = new HashMap<>();
		designInt.put("S", 0);
		designInt.put("H", 1);
		designInt.put("C", 2);
		designInt.put("D", 3);

		Map< Integer,String> intDesign = new HashMap<>();
		intDesign.put(0, "S");
		intDesign.put(1, "H");
		intDesign.put(2, "C");
		intDesign.put(3, "D");

		try {
			int N = Integer.parseInt(br.readLine()); 
			String tmp;
			while((tmp = br.readLine()) != null) {
				List<String> line = Arrays.asList(tmp.split("\\s"));
				String design = line.get(0);
				Integer num = Integer.parseInt(line.get(1));

				card[designInt.get(design)][num] = true;
				
			}
			br.close();
		}catch(IOException e) {
			e.printStackTrace();
		}

		for(int i=0;i<4;i++) {
			for(int j=1;j<14;j++) {
				if(card[i][j] == false) {
					String design= intDesign.get(i);
					System.out.printf("%s %d\n",design, j);
				}
			}
		}
					
	}
}
