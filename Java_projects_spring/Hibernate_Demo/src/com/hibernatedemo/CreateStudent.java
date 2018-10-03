package com.hibernatedemo;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import com.entity.Student;

public class CreateStudent {

	public static void main(String[] args) {
	
		SessionFactory factory= new Configuration().configure("hibernate.cfg.xml").addAnnotatedClass(Student.class)
				.buildSessionFactory();
		
		Session session=factory.getCurrentSession();
		try
		{
			System.out.println("saving student");
			Student s= new Student("tini","jain","vijay nagar","ujjain");
			session.beginTransaction();
			System.out.println("session .save ");
			session.save(s);
			session.getTransaction().commit();
		}
		finally
		{
			factory.close();
		}

	}

}
