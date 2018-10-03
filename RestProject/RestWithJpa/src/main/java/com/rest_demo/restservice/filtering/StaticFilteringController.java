package com.rest_demo.restservice.filtering;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class StaticFilteringController {
	
	@GetMapping("/getvalue")
	public SomeBean print()
	{
		return new SomeBean("value1","value2","value3");
	}

}
