package com.annotationdemo;

import org.springframework.stereotype.Component;

@Component()
public class HappyFortune implements FortunieService {

	public String getFortune() {
		
		return "constructor injection  by autowired and annotation ";
	}
	

}
