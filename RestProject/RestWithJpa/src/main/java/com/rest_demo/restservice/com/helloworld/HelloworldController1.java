package com.rest_demo.restservice.com.helloworld;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloworldController1{

	@GetMapping("/helloworld1")
	public HelloWorldBean1 helloWorld() {
		return (new HelloWorldBean1("hello world ....."));

	}

	@GetMapping("/helloworld1/pathvariable1/{name1}")
	public HelloWorldBean1 helloWorldPathvariable(@PathVariable String name1) {
		return (new HelloWorldBean1(String.format("hello world .....,%s",name1)));

	}
}
