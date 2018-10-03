package com.firstdemo;

import org.springframework.context.support.ClassPathXmlApplicationContext;

public class SetterdemoApp {

	public static void main(String[] args) {
		
	ClassPathXmlApplicationContext context=new ClassPathXmlApplicationContext("applicationContext.xml");
	CricketCoach cc=(CricketCoach)context.getBean("cricketcoach");
	System.out.println(cc.dailyWorkout());
	System.out.println(cc.getDailyServices());
	System.out.println(cc.getEmailid());
	System.out.println();
	context.close();
	}

}
