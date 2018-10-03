package com.rest_demo.restservice.user;

import java.util.Date;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.validation.constraints.Past;
import javax.validation.constraints.Size;

import org.junit.experimental.categories.Categories.ExcludeCategory;

@Entity
public class UserBean {
	@Id
	@GeneratedValue
	Integer id;
	@Size(min=3 ,message="min 3 character are requried")
	String name;
	@Past
	Date dob;
	
	public UserBean() {
		
	}
	public UserBean(Integer id, String name, Date dob) {
		super();
		this.id = id;
		this.name = name;
		this.dob = dob;
	}
	public Integer getId() {
		return id;
	}
	public void setId(Integer id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public Date getDob() {
		return dob;
	}
	public void setDob(Date dob) {
		this.dob = dob;
	}
	@Override
	public String toString() {
		return "UserBean [id=" + id + ", name=" + name + ", dob=" + dob + "]";
	}
	
}