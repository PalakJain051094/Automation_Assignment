package com.hibernatedemo;

import java.util.List;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import com.entity.Student;

public class CrudOperation {

	public static void main(String[] args) {
	
		SessionFactory factory= new Configuration().configure("hibernate.cfg.xml").addAnnotatedClass(Student.class)
				.buildSessionFactory();
		
		Session session=factory.getCurrentSession();
		try
		{
			
			session.beginTransaction();
			
			//to print all student table records.
			List<Student> thestudent=session.createQuery("from Student").getResultList();
			display(thestudent);
			//query to print student whose first name is palak
			thestudent=session.createQuery("from Student s where s.fn='palak'").getResultList();
			display(thestudent);
			session.getTransaction().commit();
			
			//update student 
			session=factory.getCurrentSession();
			session.beginTransaction();
			session.createQuery("update Student set fn='xyz' where id=3").executeUpdate();
			session.getTransaction().commit();
			
			//delete student
			session=factory.getCurrentSession();
			session.beginTransaction();
			session.createQuery("delete from Student where id=3").executeUpdate();
			session.getTransaction().commit();
			
		}
		finally
		{
			factory.close();
		}

	}

	private static void display(List<Student> thestudent) {
		for(Student s:thestudent)
		{
			System.out.println(s);
		}
	}

}
