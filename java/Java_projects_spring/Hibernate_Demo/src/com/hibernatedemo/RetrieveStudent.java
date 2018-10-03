package com.hibernatedemo;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import com.entity.Student;

public class RetrieveStudent {

	public static void main(String[] args) {
	
		SessionFactory factory= new Configuration().configure("hibernate.cfg.xml").addAnnotatedClass(Student.class)
				.buildSessionFactory();
		
		Session session=factory.getCurrentSession();
		try
		{
			System.out.println("retrieve student");
			Student s= new Student("palak","jain","vijay nagar","shajapur");
			session.beginTransaction();
			System.out.println(s);
			System.out.println("session .save ");
			session.save(s);
			session.getTransaction().commit();
			//for reterive
			
			System.out.println("student inserted is ::"+s.getId());
			session=factory.getCurrentSession();
			session.beginTransaction();
			Student stu=session.get(Student.class,s.getId());
			System.out.println(stu);
			session.getTransaction().commit();
		}
		finally
		{
			factory.close();
		}

	}

}
