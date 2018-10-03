package com.rest_demo.restservice.filtering;

import org.springframework.http.converter.json.MappingJacksonValue;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.fasterxml.jackson.databind.ser.BeanPropertyFilter;
import com.fasterxml.jackson.databind.ser.FilterProvider;
import com.fasterxml.jackson.databind.ser.impl.SimpleBeanPropertyFilter;
import com.fasterxml.jackson.databind.ser.impl.SimpleFilterProvider;

@RestController
public class DynamicFilteringController {
	
	//field1,field2
	@GetMapping("/filter")
	public MappingJacksonValue print()
	{
		SomeBean somebean=new SomeBean("value11","value22","value33");
		
		
		SimpleBeanPropertyFilter filter=SimpleBeanPropertyFilter.filterOutAllExcept("filed1","filed2");
		FilterProvider filters=new SimpleFilterProvider().addFilter("somebeanfilter", filter);
		
		MappingJacksonValue mapping=new MappingJacksonValue(somebean);
		mapping.setFilters(filters);
		return mapping;
	}
	

}
