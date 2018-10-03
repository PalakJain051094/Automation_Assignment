import java.io.File;


public class FindFile  {
	
	static String drive="D:";
	static String folder="/Files_demo";
	static String file_name="/pqr.txt";

		    public static void main(String[] args) 
		    {
		    	try
		    	{
		    	File f = new File(drive+folder+file_name);

		    	if(f.exists()){
		    	    System.out.println("File existed=.."+drive+folder+file_name);
		    	}else{
		    	    System.out.println("File not found!");
		    	}
		    	}
		    	catch(Exception e)
		    	{
		    		e.printStackTrace();
		    	}
		      
		    }

}
