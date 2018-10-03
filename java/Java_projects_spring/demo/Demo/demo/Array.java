package demo;

import java.util.Scanner;

public class Array {
	Scanner sc=new Scanner(System.in);
	int arr [];
	public void fun()
	{
		arr=new int[5];
		System.out.println("enter array");
		for(int i=0;i<5;i++)
		{
			arr[i]=sc.nextInt();
			

			System.out.println(arr[i]);
			}

	}
	public static void main(String argus[])
	{
		Array a=new Array();
		a.fun();	}

}
