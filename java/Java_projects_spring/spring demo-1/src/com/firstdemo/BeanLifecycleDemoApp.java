package com.firstdemo;

import org.springframework.context.support.ClassPathXmlApplicationContext;

public class BeanLifecycleDemoApp {

	public static void main(String[] args) {
		
		ClassPathXmlApplicationContext context=new ClassPathXmlApplicationContext("BeanLifecycle-ApplicationContext.xml");
		Coach coach2=(Coach) context.getBean("mycoach1");
		System.out.println(coach2.dailyWorkout());
		context.close();
	}

}
