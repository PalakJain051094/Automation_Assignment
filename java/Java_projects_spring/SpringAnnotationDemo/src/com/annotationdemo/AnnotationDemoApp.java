package com.annotationdemo;

import org.springframework.context.support.ClassPathXmlApplicationContext;

public class AnnotationDemoApp {

	public static void main(String[] args) {
		ClassPathXmlApplicationContext context=new ClassPathXmlApplicationContext("applicationContext.xml");
		Coach c=(TennisCoach) context.getBean("tenniscoachid");
		// deafult bean id ---->Coach c1=(TennisCoach) context.getBean("tennisCoach");
		System.out.println(c.getDailyWorkout());
		System.out.println(c.getDailyFortune());
		context.close();

	}

}
