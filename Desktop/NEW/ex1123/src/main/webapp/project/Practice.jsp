<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>

<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions"%>
<c:set var="contextPath" value="${pageContext.request.contextPath}" />


<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>연습</title>
</head>
<body>

	<!-- controller에서 객체바인딩한 vo -->
	<p>세션정보 아이디 : ${vo.id}</p>
	<p>세션정보 비밀번호 : ${vo.pw}</p>
	<c:forEach var="i" items="${list}">
		<tr>
			<td>${i.id}</td>
			<td>${i.pw}</td>
		</tr>
		<br>
	</c:forEach>
	
	<button onclick="location.href='${contextPath}/MainPage.do'">메인페이지로 돌아가기</button>	
</body>
</html>