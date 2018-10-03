package com.firstdemo;

public class CricketCoach implements Coach{

	private FortunieService fcc;
	private String emailid;
	private String team;
	public CricketCoach() {
		System.out.println("cricket coach class constructor");;
	}
	public String dailyWorkout() {
		
		return "doing cricket practice";
	}

	public String getDailyServices() {
		
		return "cricketcoach" + fcc.getServices();
	}
	public String getEmailid() {
		
		return emailid;
	}
	public void setEmailid(String emailid) {
		System.out.println("emailid");
		this.emailid = emailid;
	}
	public String getTeam() {
		return team;
	}
	public void setTeam(String team) {
		System.out.println("team");
		this.team = team;
	}
	public void setFcc(FortunieService fcc) {
		System.out.println("setter method of crciket coach class");
		this.fcc = fcc;
	}

}
