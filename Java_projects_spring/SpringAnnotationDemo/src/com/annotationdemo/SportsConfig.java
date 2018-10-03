package com.annotationdemo;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
//@ComponentScan("com.annotationdemo")
public class SportsConfig {
	
	//define bean for setFortune service
	@Bean
	public FortunieService setFortunieService()
	{
		return new SetFortuneService();
	}
	
@Bean
public Coach swimCoach()
{
	return new SwimCoach(setFortunieService());
}

}
