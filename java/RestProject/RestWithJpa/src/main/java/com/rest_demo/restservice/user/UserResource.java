package com.rest_demo.restservice.user;

import java.net.URI;
import java.util.List;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.hateoas.Resource;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.hateoas.mvc.ControllerLinkBuilder;
import org.springframework.hateoas.mvc.ControllerLinkBuilder.*;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;
@RestController
public class UserResource {
	@Autowired
	private UserDaoService userservice1;
	

	@GetMapping(path="/users")
	public List<UserBean> all()
	{
		return userservice1.findAll();
	}
	@GetMapping("/users/{id}")
	public UserBean one(@PathVariable int id)
	{
		UserBean user=userservice1.findOne(id);
		if(user==null)
		{
			throw new UserNotFoundException("id"+id);
		}
		
		return user;
	}

	@PostMapping("/createuser")
	public ResponseEntity<Object>createUser(@Valid @RequestBody UserBean user)
	{
		UserBean saveduser=userservice1.save(user);
		
		URI uri = ServletUriComponentsBuilder.fromCurrentRequest().path("/{id}").
				buildAndExpand(saveduser.getId()).toUri();
		
		return ResponseEntity.created(uri).build();
		
	}
	@DeleteMapping("/deleteuser/{id}")
	public void deleteUser(@PathVariable int id)
	{
		UserBean user=userservice1.deleteById(id);
		if(user==null)
		{
			throw new UserNotFoundException("id"+id);
		}
	}
}




