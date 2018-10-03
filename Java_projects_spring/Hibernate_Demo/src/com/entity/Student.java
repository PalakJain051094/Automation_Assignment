package com.entity;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;



@Entity
@Table(name="student")
public class Student {
@Id
@Column(name="student_id")
	int id;
@Column(name="firstname")
	String fn;
@Column(name="lastname")
	String ln;
@Column(name="address")
	String add;
@Column(name="city")
	String city;

	public Student(String fn, String ln, String add, String city) {
	super();

	this.fn = fn;
	this.ln = ln;
	this.add = add;
	this.city = city;
}


	@Override
	public String toString() {
		return "Student [id=" + id + ", fn=" + fn + ", ln=" + ln + ", add="
				+ add + ", city=" + city + "]";
	}


	public Student() {
		
	}

	
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getFn() {
		return fn;
	}
	public void setFn(String fn) {
		this.fn = fn;
	}
	public String getLn() {
		return ln;
	}
	public void setLn(String ln) {
		this.ln = ln;
	}
	public String getAdd() {
		return add;
	}
	public void setAdd(String add) {
		this.add = add;
	}
	public String getCity() {
		return city;
	}
	public void setCity(String city) {
		this.city = city;
	}
}
