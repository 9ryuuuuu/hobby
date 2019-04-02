import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int S = sc.nextInt();

		System.out.printf("%d:%d:%d\n", S/(60*60),(S%(60*60))/60,S%60);
	}

}
