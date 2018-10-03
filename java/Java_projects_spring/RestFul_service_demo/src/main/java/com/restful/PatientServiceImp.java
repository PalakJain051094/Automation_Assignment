package com.restful;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Service;

import com.restful.model.Patient;


public class PatientServiceImp implements PatientService{

	Map<Long, Patient> po = new HashMap<>();
	long currentid=123;
	public PatientServiceImp()
	{
		init();
	}
	
	public void init()
	{
		Patient p=new Patient();
		p.setId(currentid);
		p.setName("john");
		po.put(p.getId(),p);
	}

	@Override
	public List<Patient> getPatients() {
		    
	Collection<Patient> results = po.values();
	List response = new ArrayList(results);
	System.out.println("hello");
		return response;
	}
	
}
 

 


