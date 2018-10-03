package com.annotationdemo;

import org.springframework.stereotype.Component;

@Component
public class RestFortuneService implements FortunieService {

	public String getFortune() {
		
		return "RestFortuneService";
	}

}
