package com.firstdemo;

public class BaseballCoach implements Coach{
	
	private FortunieService fs;
	
	

	public BaseballCoach(FortunieService fs) {
		super();
		this.fs = fs;
	}

	public String dailyWorkout()
	{
		return "Iam doing my dailyworkout";
	}

	public String getDailyServices() {
		
		return fs.getServices();
	}

}
