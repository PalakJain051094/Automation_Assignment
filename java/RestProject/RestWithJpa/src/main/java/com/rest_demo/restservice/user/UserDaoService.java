package com.rest_demo.restservice.user;

import java.util.ArrayList;
import java.util.Date;
import java.util.Iterator;
import java.util.List;

import org.springframework.stereotype.Component;

@Component
public class UserDaoService {
	
public static List<UserBean> users=new ArrayList<UserBean>();

private static int usercount=3;
	
	static
	{
		users.add(new UserBean(1,"palak",new Date()));
		users.add(new UserBean(2,"Tini",new Date()));
		users.add(new UserBean(3,"pooja",new Date()));
	}
	
	public List<UserBean> findAll()
	{
		return users;
		
	}
	
	public UserBean save(UserBean user)
	{
		if(user.getId()==null)
		{
			user.setId(++usercount);
		}
		users.add(user);
		return user;
		
	}
	public UserBean findOne(int id)
	{
		for(UserBean user:users)
		{
			if(user.getId()==id)
			{
				return user;
			}
		}
		return (UserBean) users;
	}
	public UserBean deleteById(int id)
	{
		Iterator<UserBean> iterator=users.iterator();
		while(iterator.hasNext())
		{
		UserBean user=iterator.next();
		if(user.getId()==id)
		{
			iterator.remove();
			return user;
		}
		}
		return null;
		
	}
}
