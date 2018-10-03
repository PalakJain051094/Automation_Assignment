package com.annotationdemo;

import org.springframework.context.support.ClassPathXmlApplicationContext;

public class AnnotationBeanScopeDemoApp {

	public static void main(String[] args) {
		ClassPathXmlApplicationContext context=new ClassPathXmlApplicationContext("applicationContext.xml");
		Coach c=(Coach) context.getBean("tenniscoachid");
		Coach c1=(Coach) context.getBean("tenniscoachid");
		boolean result=(c==c1);
		System.out.println("result of scope"+result);
		System.out.println("memory location for c"+c);
		System.out.println("memory location for c1"+c1);
		context.close();
	}

}
