package com.restful;

import javax.ws.rs.GET;
import javax.ws.rs.Path;

import java.util.*;

import com.restful.model.*;
@Path("/patientservice")
public interface PatientService {
	
	@Path("/patients")
	@GET
	List<Patient> getPatients();

}
