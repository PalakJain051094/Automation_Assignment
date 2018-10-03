<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
 <%@taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Customer Form</title>
<style>
.error{color.Red}
</style>
</head>
<body>
<form:form action="processCustomer" modelAttribute="customer">
first name:::<form:input path="firstname"/>
</br>
lastname(*):::<form:input path="lastname"/>
<form:errors path="lastname" cssClass="error"></form:errors>
</br>
<input type="submit" value="submit"/>
</form:form>
</body>
</html>