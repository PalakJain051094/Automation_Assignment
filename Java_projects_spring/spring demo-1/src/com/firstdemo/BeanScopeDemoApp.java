package com.firstdemo;

import org.springframework.context.support.ClassPathXmlApplicationContext;

public class BeanScopeDemoApp {

	public static void main(String[] args) {
		
		ClassPathXmlApplicationContext context=new ClassPathXmlApplicationContext("BeanScope-ApplicationContext.xml");
		Coach coach=(Coach) context.getBean("mycoach");
		Coach coach1=(Coach) context.getBean("mycoach");
		boolean result=(coach==coach1);
		System.out.println("result for singleton refer to same memory::"+result);
		System.out.println("coach memeory area"+coach);
		System.out.println("coach1 memeory area"+coach1);
		context.close();
	}

}
