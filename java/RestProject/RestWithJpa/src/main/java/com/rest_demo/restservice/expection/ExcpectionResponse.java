package com.rest_demo.restservice.expection;

import java.util.Date;

public class ExcpectionResponse {
	Date timestamp;
	String messages;
	String details;
	public ExcpectionResponse(Date timestamp, String messages, String details) {
		super();
		this.timestamp = timestamp;
		this.messages = messages;
		this.details = details;
	}
	public Date getTimestamp() {
		return timestamp;
	}
	public String getMessages() {
		return messages;
	}
	public String getDetails() {
		return details;
	}
	
	

}
