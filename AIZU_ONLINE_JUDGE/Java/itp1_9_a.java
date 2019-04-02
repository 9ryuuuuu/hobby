import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Main {

	public static void main(String[] args) {
//		String baseUrl = "C:\\Users\\kuriyama.akira\\git-repository\\hobby\\AIZU_ONLINE_JUDGE\\Java\\";
//		String filePath = baseUrl +  "inp_itp_1_9_a.txt";
//		FileInputStream fis = null; 
//		try { 
//			fis = new FileInputStream(new File(filePath));
//		}catch(FileNotFoundException e){
//			e.printStackTrace();
//		}
//		BufferedReader br = new BufferedReader(new InputStreamReader(fis));
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		List<String> ti = new ArrayList<String>();
		int cnt = 0;
		
		String W = "";
		try {
			W = br.readLine(); 
			String tmp;
			while((tmp = br.readLine()) != null) {
				if(tmp.equals("END_OF_TEXT"))break;
				
				List<String> line = Arrays.asList(tmp.split("\\s"));
				ti.addAll(line);
				ti = ti.stream().map(t -> t.toLowerCase()).collect(Collectors.toList());
			}
			br.close();
		}catch(IOException e) {
			e.printStackTrace();
		}

		for(String hoge: ti) {
			if(hoge.equals(W))
				cnt++;
		}
		System.out.println(cnt);		
	}
}
