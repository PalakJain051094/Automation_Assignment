package com.firstdemo;

import org.springframework.context.support.ClassPathXmlApplicationContext;

public class HelloSpring {

	public static void main(String[] args) {
		
		//Configuration
		ClassPathXmlApplicationContext context= new ClassPathXmlApplicationContext("applicationContext.xml");
	
		//retrieve bean from container
		Coach thecoach=(Coach) context.getBean("mycoach","Coach.class");
		
		System.out.println(thecoach.dailyWorkout());
		System.out.println(thecoach.getDailyServices());
		context.close();
	}

}
