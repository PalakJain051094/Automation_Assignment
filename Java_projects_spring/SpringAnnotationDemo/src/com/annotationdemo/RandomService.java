package com.annotationdemo;

import org.springframework.stereotype.Component;

@Component
public class RandomService implements FortunieService{

	public String getFortune() {
	
		return "Random service claass method.....";
	}

}
