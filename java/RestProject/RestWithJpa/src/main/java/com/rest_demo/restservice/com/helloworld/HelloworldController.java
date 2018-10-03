package com.rest_demo.restservice.com.helloworld;

import java.util.Locale;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.MessageSource;
import org.springframework.context.i18n.LocaleContextHolder;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloworldController {
	
	@Autowired
	MessageSource messagesource;

	@GetMapping("/helloworld")
	public HelloWorldBean helloWorld() {
		return (new HelloWorldBean("hello world ....."));

	}

	@GetMapping("/helloworld/pathvariable/{name}")
	public HelloWorldBean helloWorldPathvariable(@PathVariable String name) {
		return (new HelloWorldBean(String.format("hello world .....,%s",name)));

	}
	
	@GetMapping("/hello/internationalization")
	public String helloMessage(@RequestHeader(name="Accept-Language",required=false)Locale locale)
	{
		return messagesource.getMessage("good.message",null, LocaleContextHolder.getLocale()) ;
	
	}
}

