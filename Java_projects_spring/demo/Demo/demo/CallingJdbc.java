package demo;

import java.sql.CallableStatement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class CallingJdbc {
	Connection con;
	Connection con1;
	public void calling() throws ClassNotFoundException
	{
		Class.forName("com.mysql.jdbc.Driver");  
		try {
			Connection con=DriverManager.getConnection(  
			"jdbc:mysql://127.0.0.1:3306/demo_database","palak","palak");
			Statement st=con.createStatement();
			ResultSet rs=st.executeQuery("select * from emp");
			while(rs.next())
			{
				System.out.println(rs.getInt(1));
			}
			CallableStatement cs=con1.prepareCall("call sp_CursorDemo()");
			System.out.println("after prepare call");
			cs.execute();
			System.out.println("afterr execute of cs");
			
		} catch (SQLException e) {
		 	
			e.printStackTrace();
		}  
		
		
	}
	

	public static void main(String[] args) throws ClassNotFoundException {
		CallingJdbc cj=new CallingJdbc();
		cj.calling();
		

	}

}