import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(sc.hasNext()) {
			int a = sc.nextInt();
			String op = sc.next();
			int b = sc.nextInt();
			if(op.equals("?")) {
				break;
			}else if(op.equals("+")) {
				System.out.println(a + b);
			}else if(op.equals("-")) {
				System.out.println(a - b);
			}else if(op.equals("*")) {
				System.out.println(a * b);
			}else if(op.equals("/")) {
				System.out.println(a / b);
			}
			
			
		}
	
	}
}
