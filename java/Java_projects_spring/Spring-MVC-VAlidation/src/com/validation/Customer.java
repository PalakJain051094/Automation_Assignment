package com.validation;

import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;

public class Customer {
	String firstname;
	@NotNull(message="last name is requried")
	@Size(min=3,message="name is requried")
	String lastname;
	public String getFirstname() {
		return firstname;
	}
	public void setFirstname(String firstname) {
		this.firstname = firstname;
	}
	public String getLastname() {
		return lastname;
	}
	public void setLastname(String lastname) {
		this.lastname = lastname;
	}

}
