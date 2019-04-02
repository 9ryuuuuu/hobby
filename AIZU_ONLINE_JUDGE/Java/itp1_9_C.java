import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;

public class Main {

	public static void main(String[] args) {
//		String baseUrl = "C:\\Users\\kuriyama.akira\\git-repository\\hobby\\AIZU_ONLINE_JUDGE\\Java\\";
//		String filePath = baseUrl +  "inp_itp_1_9_c.txt";
//		FileInputStream fis = null; 
//		try { 
//			fis = new FileInputStream(new File(filePath));
//		}catch(FileNotFoundException e){
//			e.printStackTrace();
//		}
//		BufferedReader br = new BufferedReader(new InputStreamReader(fis));
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int taro = 0;
		int hana = 0;
		
		try {
			int N = Integer.parseInt(br.readLine()); 
			String tmp;
			while((tmp = br.readLine()) != null) {
				
				List<String> line = Arrays.asList(tmp.split("\\s"));
				String taroC = line.get(0);
				String hanaC = line.get(1);
				int result =taroC.compareTo(hanaC); 
				if(result ==0) {
					taro++;
					hana++;
				}else if(result >0) {
					taro+=3;
				}else {
					hana+=3;
				}
			}
			br.close();
		}catch(IOException e) {
			e.printStackTrace();
		}

		System.out.printf("%d %d\n",taro,hana);		
	}
}
