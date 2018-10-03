package com.rest_demo.restservice.versioning;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PersonController {
	
	@GetMapping("/v1")
	public PersonV1 personV1()
	{
		return new  PersonV1("palak Jain");
	}

	@GetMapping("/v2")
	public PersonV2 personV2()
	{
		return new  PersonV2(new Name("palak","jain"));
	}
	//params
	@GetMapping(value="/person/param",params="version=1")
	public PersonV1 personVesrion1()
	{
		return new  PersonV1("palak Jain");
	}

	@GetMapping(value="/person/param",params="version=2")
	public PersonV2 personVersion2()
	{
		return new  PersonV2(new Name("palak","jain"));
	}
	//headers
	@GetMapping(value="/person/header",headers="version=1")
	public PersonV1 personHeader1()
	{
		return new  PersonV1("palak Jain");
	}

	@GetMapping(value="/person/header",headers="version=2")
	public PersonV2 personHeader2()
	{
		return new  PersonV2(new Name("palak","jain"));
	}
	//produces
	@GetMapping(value="/person/produces",produces="application/vnd.company.app-v1+json")
	public PersonV1 personProducer1()
	{
		return new  PersonV1("palak Jain");
	}

	@GetMapping(value="/person/produces",produces="application/vnd.company.app-v2+json")
	public PersonV2 personProcedure2()
	{
		return new  PersonV2(new Name("palak","jain"));
	}
}
