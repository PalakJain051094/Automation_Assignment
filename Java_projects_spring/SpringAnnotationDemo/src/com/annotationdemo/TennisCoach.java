package com.annotationdemo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;
import org.springframework.web.bind.annotation.PostMapping;

// default bean id ---->@Component()

@Component("tenniscoachid")
@Scope()
public class TennisCoach implements Coach {
	
	@Autowired
	@Qualifier("happyFortune")
	private FortunieService fc;
	
	/* CONSTRUCTOR INJECTION 
	@Autowired
	public TennisCoach(FortunieService fc) {
		
		this.fc = fc;
	}*/

	public TennisCoach() {
		System.out.println("TENNIS COACH Default ocnstructor");
	}

	/* seeter injection 
	  @Autowired	
	 
	public void setFc(FortunieService fc) {
		System.out.println("in setter method of tennis coach class ");
		this.fc = fc;
	}*/
	
	/* method injection
	@Autowired	
		public void haveFun(FortunieService fc) {
			System.out.println("in have fun method of tennis coach class ");
			this.fc = fc;
	 }*/

	public String getDailyWorkout() {
		
		return "Do hard work to win::;";
	}

	public String getDailyFortune() {
		
		return fc.getFortune();
	}
	
	
}
