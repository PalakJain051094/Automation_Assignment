package com.onetoone_mapping;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.OneToOne;
import javax.persistence.Table;

@Entity
@Table(name="instructor")
public class Instructor {
	@Id
	@Column(name="id")
	int id;
	@Column(name="first_name")
	String fn;
	@Column(name="last_name")
	String ln;
	@Column(name="email")
	String email;
	@OneToOne(cascade=CascadeType.ALL)
	@JoinColumn(name="instructor_detail_id",referencedColumnName="id")
	Instructor_Detail detail;
	public Instructor() {
		
	}
	@Override
	public String toString() {
		return "Instructor [id=" + id + ", fn=" + fn + ", ln=" + ln
				+ ", email=" + email + ", detail=" + detail + "]";
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
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public Instructor_Detail getDetail() {
		return detail;
	}
	public void setDetail(Instructor_Detail detail) {
		this.detail = detail;
	}
	public Instructor(String fn, String ln, String email) {
		
		this.fn = fn;
		this.ln = ln;
		this.email = email;
	}
	
	
	 
	 

}
