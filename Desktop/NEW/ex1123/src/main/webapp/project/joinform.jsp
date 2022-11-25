<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
    
    
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions"%>
<c:set var="contextPath" value="${pageContext.request.contextPath}" />
    
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<h1>회원가입하기</h1>
	<form action="${contextPath}/signup.do" method="get">
<div class="form-group">
	<input type="text" class="form-control" placeholder="아이디" name="id" maxlength="20">
</div>
<div class="form-group">
	<input type="password" class="form-control" placeholder="비밀번호" name="pw" maxlength="20">
</div>
<div class="form-group">
	<input type="text" class="form-control" placeholder="이름" name="name" maxlength="20">
</div>
<div class="form-group" style="text-align: center;">
	<div class="btn-group" data-toggle="buttons">
		<label class="btn btn-primary active">
			<input type="radio" name="gender" autocomplete="off" value="남자" checked>남자
        </label>
        <label class="btn btn-primary">
        	<input type="radio" name="gender" autocomplete="off" value="여자" checked>여자
        </label>
	</div>
</div>
<div class="form-group">
	<input type="email" class="form-control" placeholder="이메일" name="email" maxlength="20">
</div>
	<button type="submit">JOIN</button>
</form>
</div>

</body>
</html>