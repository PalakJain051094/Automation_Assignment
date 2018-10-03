package demo;

import java.util.Scanner;
//3may2018
public class NonrepArray {

	Scanner sc = new Scanner(System.in);
	int arr[];
	int n;

	int flag = 0;

	public void fun() {
		System.out.println("enter size");
		n = sc.nextInt();
		System.out.println("enter array");
		arr = new int[n];
		for (int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}
	}

	public void cal() {

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (i != j) {
					if (arr[i] == arr[j]) {
						flag = 0;
						break;
					}
					if (arr[i] != arr[j]) {
						flag = 1;

					}
				}

			}
			if (flag == 1) {
				System.out.println("non reptable element:::"+arr[i]);
				}

		}
	}

	public static void main(String[] args) {
		NonrepArray na = new NonrepArray();
		na.fun();
		na.cal();

	}

}
