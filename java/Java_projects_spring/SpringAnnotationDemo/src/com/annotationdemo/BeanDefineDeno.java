package com.annotationdemo;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class BeanDefineDeno {

	public static void main(String[] args) {
		AnnotationConfigApplicationContext context=new AnnotationConfigApplicationContext(SportsConfig.class);
		Coach c= context.getBean("swimCoach",Coach.class);
		// deafult bean id ---->Coach c1=(TennisCoach) context.getBean("tennisCoach");
		System.out.println(c.getDailyWorkout());
		System.out.println(c.getDailyFortune());
		context.close();

	}

}
