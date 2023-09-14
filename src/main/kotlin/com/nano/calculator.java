package calculator_application;

import java.util.Scanner;

public class calculator {
	public static String greetings() {
		return "Hello World!";
	}
	public static int add(int a,int b) {
		return a+b;
	}
	public static int sub(int a,int b) {
		return a-b;
	}


	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		System.out.println("enter first number");
		int first_number =sc.nextInt();
		System.out.println("enter second number");
		int second_number=sc.nextInt();
		System.out.println("Choose any number[0,1,2] to perform addition and subtraction");
		int n= sc.nextInt();

		switch(n) {
		case 0:
			System.out.println(greetings());
		case 1: 
			System.out.println(add(first_number,second_number));
			break;
		case 2: 
			System.out.println(sub(first_number,second_number));
			break;
		default:
			System.out.println("please provide valid number");
		}
	}

}
