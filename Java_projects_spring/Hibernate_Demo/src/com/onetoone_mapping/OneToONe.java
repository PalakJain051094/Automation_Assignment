package com.onetoone_mapping;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class OneToONe {

	public static void main(String[] args) {
		SessionFactory factory=new Configuration().configure("hibernate.cfg.xml").addAnnotatedClass(Instructor.class)
				.addAnnotatedClass(Instructor_Detail.class).buildSessionFactory();
		Session session=factory.getCurrentSession();
		try
		{
			Instructor i=new Instructor("palak","jain","palka@gmail.com");
			Instructor_Detail details=new Instructor_Detail("palak.rocks","writting**");
			i.setDetail(details);
			session.beginTransaction();
			System.out.println("saving object");
			session.save(i);
			session.getTransaction().commit();
			
		}
		catch(Exception e)
		{
			System.out.println(e);
		}
	
		finally
		{
			factory.close();
		
		}
		
		
	}

}
