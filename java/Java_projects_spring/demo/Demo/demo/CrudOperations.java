package demo;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

public class CrudOperations {
	Connection con;
	Scanner sc= new Scanner(System.in);
	int id=0;
	String ln,fn,add,city=null;
	public void connectionMethod()
	{
		try
		{
			Class.forName("com.mysql.jdbc.Driver");
			con=DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/demo_database","palak","palak");
			
		}
		catch(Exception ex)
		{
			System.out.println(ex);
		}
		
	}
			public void selectMethod() throws SQLException
		{
			System.out.println("enter id ");
			id=sc.nextInt();
			Statement st;
			ResultSet rs;
			st=con.createStatement();
			rs=st.executeQuery("select * from emp where empid ="+id);
			while(rs.next())
			{
				System.out.println("LastName: ="+rs.getString(2));
				System.out.println("FirstName:="+rs.getString(3));
				System.out.println("Address:= "+rs.getString(4));
				System.out.println("City:= "+rs.getString(5));
			}
			}
		public void insertmethod()
		{
			System.out.println("enter data to be insert in table");
			System.out.println("enetr id");
			id=sc.nextInt();
			System.out.println("enetr last name");
			ln=sc.next();
			System.out.println("enetr first name");
			fn=sc.next();
			System.out.println("enetr address");
			add=sc.next();
			System.out.println("enetr city");
			city=sc.next();
			String insert_query="insert into emp (empId,LastName,FirstName,Address,City) values(?,?,?,?,?)";
			try {
				PreparedStatement ps=con.prepareStatement(insert_query);
				int rs=0;
				ps.setInt(1, id);
				ps.setString(2, ln);
				ps.setString(3, fn);
				ps.setString(4, add);
				ps.setString(5, city);
				rs=ps.executeUpdate();
				if(rs>0)
				{
					System.out.println("data inserted succesfully for id "+id);
				}
				
				
			} catch (SQLException e) {
				
				e.printStackTrace();
			}
			
			 
			
			 
			 }
public void deleteMethod()
{
	try {
		System.out.println("enter id for which you want to delete record from table");
		System.out.println("enetr id");
		id=sc.nextInt();
		Statement st;
		int rs=0;
		st=con.createStatement();
		rs=st.executeUpdate("delete  from emp where empId="+id);
		if(rs>0)
			System.out.println("record deleted for id "+id);
	
	} catch (SQLException e) {
		
		e.printStackTrace();
	}
}
	
public void updateMethod()
{
		System.out.println("enter id to be update in table");
		System.out.println("enetr id");
		id=sc.nextInt();
		updateHistory_Table( id);
		System.out.println("enter address");
		String address = sc.next();
		String upadte_query="update emp set Address = ? where empId="+id ;
		
		try {
			PreparedStatement ps=con.prepareStatement(upadte_query);
			int rs=0;
			ps.setString(1,address);
			
			rs=ps.executeUpdate();
			if(rs>0)
			{
				System.out.println("data updated succesfully for id "+id);
				
				
			}
			
			
		} catch (SQLException e) {
			
			e.printStackTrace();
		}
		
}

public void update_emp_history()
{
	
}
public void updateHistory_Table(int id)
{
	String sql="insert into emp_history (select *  from emp where empId="+id+")";
	// this not work ----String sql="select * into emp_history from emp where empId="+id;
	Statement st;
	int rs1=0;
	try {
		st = con.createStatement();
		rs1=st.executeUpdate(sql);
		

		if(rs1>0 )
		{
			System.out.println("data inserted in to emp_history table");
		}
		
			
	} catch (SQLException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
	
}
	
	public static void main(String args[]) throws SQLException
	{
		CrudOperations co=new CrudOperations();
		co.connectionMethod();
		//co.selectMethod();
		//co.insertmethod();
		//co.deleteMethod();
		co.updateMethod();
		
	}

}
