package com.rest_demo.restservice;

import java.util.Locale;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;
import org.springframework.context.support.ResourceBundleMessageSource;
import org.springframework.web.servlet.i18n.AcceptHeaderLocaleResolver;
import org.springframework.web.servlet.i18n.SessionLocaleResolver;

@SpringBootApplication

public class RestserviceApplication {

	public static void main(String[] args) {
		SpringApplication.run(RestserviceApplication.class, args);
	}
	//Internationalization

	@Bean
	public AcceptHeaderLocaleResolver local()
	{
		AcceptHeaderLocaleResolver slr=new AcceptHeaderLocaleResolver();
	slr.setDefaultLocale(Locale.US);		
	return slr;
		}
	
	/*@Qualifier
	public ResourceBundleMessageSource resourcebundle()
	{
	ResourceBundleMessageSource rbms=new ResourceBundleMessageSource();
		rbms.setBasename("message");
		return rbms;
		
	}*/
}
