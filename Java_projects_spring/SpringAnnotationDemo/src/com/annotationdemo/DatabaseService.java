package com.annotationdemo;

import org.springframework.stereotype.Component;

@Component
public class DatabaseService implements FortunieService{

	public String getFortune() {
		
		return "DAtaabse fortune service";
	}

}
