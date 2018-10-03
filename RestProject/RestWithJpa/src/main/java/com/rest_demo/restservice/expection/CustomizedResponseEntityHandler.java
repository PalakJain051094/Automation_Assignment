package com.rest_demo.restservice.expection;

import java.util.Date;

import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.context.request.WebRequest;
import org.springframework.web.servlet.NoHandlerFoundException;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;

@ControllerAdvice
@RestController
public class CustomizedResponseEntityHandler extends ResponseEntityExceptionHandler {

	public final ResponseEntity<Object> handleAllException(Exception ex,WebRequest request)
{
	ExcpectionResponse excpectionResponse = new ExcpectionResponse(new Date(), ex.getMessage(),
			request.getDescription(false));
	return ( new ResponseEntity(excpectionResponse,HttpStatus.INTERNAL_SERVER_ERROR));
	
}
	@Override
	protected ResponseEntity<Object> handleMethodArgumentNotValid(MethodArgumentNotValidException ex,
			HttpHeaders headers, HttpStatus status, WebRequest request) {
		ExcpectionResponse excpectionResponse = new ExcpectionResponse(new Date(), ex.getMessage()
				,ex.getBindingResult().toString());
		return new ResponseEntity(excpectionResponse,HttpStatus.BAD_REQUEST);
	}
}
	

