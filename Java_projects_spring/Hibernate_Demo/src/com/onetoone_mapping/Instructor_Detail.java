package com.onetoone_mapping;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name="instructor_detail")
public class Instructor_Detail {
	@Id
	@Column(name="id")
	int id;
	@Column(name="youtube_channel")
	String channel;
	@Column(name="hobby")
	String hobby;
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getChannel() {
		return channel;
	}
	public void setChannel(String channel) {
		this.channel = channel;
	}
	public String getHobby() {
		return hobby;
	}
	public void setHobby(String hobby) {
		this.hobby = hobby;
	}
	@Override
	public String toString() {
		return "Instructor_Detail [id=" + id + ", channel=" + channel
				+ ", hobby=" + hobby + "]";
	}

	public Instructor_Detail( String channel, String hobby) {
		
		this.channel = channel;
		this.hobby = hobby;
	}
	
	
	
	   
	

}
