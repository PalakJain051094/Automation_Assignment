package com.rest_demo.restservice.com.helloworld;

public class HelloWorldBean1 {
	String msg;

	public HelloWorldBean1(String msg) {
		super();
		this.msg = msg;
	}

	public String getMsg() {
		return msg;
	}

	public void setMsg(String msg) {
		this.msg = msg;
	}

	@Override
	public String toString() {
		return "HelloWorldBEan [msg=" + msg + "]";
	}
	

}
