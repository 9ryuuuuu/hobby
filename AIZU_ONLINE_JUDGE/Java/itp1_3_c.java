import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(sc.hasNext()) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			if((a==0) && (b==0)) {
				break;
			}
				
			if(a <= b) {
				System.out.printf("%d %d\n", a, b);
			}else {
				System.out.printf("%d %d\n", b, a);
			}
		}

	}
}
