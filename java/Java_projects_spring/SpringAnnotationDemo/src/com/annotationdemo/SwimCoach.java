package com.annotationdemo;

public class SwimCoach implements Coach {
	private FortunieService fc;

	public SwimCoach(FortunieService fc) {
		super();
		this.fc = fc;
	}

	public String getDailyWorkout() {
	
		return "Swim COAch get daily workout";
	}

	public String getDailyFortune() {
		
		return "swim coach get dialy fortune"+fc.getFortune();
	}

}
