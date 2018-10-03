package com.validation;


import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/customer")
public class CustomerController {
	@RequestMapping
	public String display()
	{
		return "Customer-form";
		
	}
	@RequestMapping("/showcustomer")
	public String showCustomer(Model themodel)
	
	{
		Customer cus=new  Customer();
		themodel.addAttribute("customer-model",cus);
		return "Customer-form";
	}
	
	@RequestMapping("/processCustomer")
	public String processCustomer(@Valid @ModelAttribute("customer-model")Customer cus, BindingResult br)
	{
		if(br.hasErrors())
		{
			return "Customer-form";
		}
		else
		{	
		return "Customer-submit";
		}
		
	}


}
