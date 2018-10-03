package com.firstdemo;

public class TrackCoach implements Coach {

	public String dailyWorkout() {
		// TODO Auto-generated method stub
		return "working hard";
	}

	public String getDailyServices() {
	
		return "get daily service method from trackcoach" ;
	}
	
	//init method
	
	public void initMethodFun()
	{
		System.out.println("init method");
	}
	
	//destory method
	public void destoryMethodFun()
	{
		System.out.println("destory method");
	}

}
