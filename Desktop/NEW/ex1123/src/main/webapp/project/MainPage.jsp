<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>

<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions"%>
<c:set var="contextPath" value="${pageContext.request.contextPath}" />

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>메인페이지</title>
</head>
<body>
	<!--로그인 세션 정보가 없을 때 -->
	<c:if test="${empty loginVO}">

		<form action="${contextPath}/Login.do">
			<label for="id">ID:</label> <input type="text" name="id">
			<label for="pw">Password:</label> <input type="password" name="pw">
			<button type="submit">로그인</button>
		</form>

	</c:if>
	<!--로그인 세션 정보가 있을 때 -->
	<c:if test="${!empty loginVO}">

		<form action="${contextPath}/Logout.do">
			<label>${loginVO.id}님 환영</label>
			<button type="submit">로그아웃</button>
		</form>

	</c:if>
	
	<br>
	<!--메인 페이지 컨트롤러에서 셋어트리뷰트 한 vo의 정보들을 반복문을 통해 출력하기(현재는 데이터가 1개뿐이지만 여러개일경우 반복문필요 -->
	<c:forEach var="i" items="${vo}">
		<tr>
			<td>${i.id}</td>
			<td>${i.pw}</td>
		</tr>
	</c:forEach>
	
	<br>
	<br>
	<a href="javascript:kakaoLogin();"><img src = "https://img.eduwill.net/Img2/mobile2/brand_new/common/btn-kakao-mobile@3x.png" /></a>
	<a href="javascript:kakaoLogout();">로그아웃</a>
	
	<button type="button" class="btn btn-primary"
							onclick="location.href='${contextPath}/signupform.do'">회원가입</button>
	
	
	<script src="https://t1.kakaocdn.net/kakao_js_sdk/2.0.1/kakao.min.js"
  integrity="sha384-eKjgHJ9+vwU/FCSUG3nV1RKFolUXLsc6nLQ2R1tD0t4YFPCvRmkcF8saIfOZNWf/" crossorigin="anonymous"></script>
    <script src="https://developers.kakao.com/sdk/js/kakao.js"></script>
    
    <script>
      Kakao.init("bdfb36e86a1ae429034490f7c256dff1");


      function kakaoLogin() {
        window.Kakao.Auth.login({
          scope: "profile_nickname,account_email",
          success: (authObj) => {
            console.log("authObj : ");
            console.log(authObj);

            // 백한테 authobj 속 access토큰만 줌
            // 그 후 authorize를 통해 확인
            window.Kakao.API.request({
              url: "/v2/user/me",
              success: (res) => {
                console.log("success: ");
                console.log(res);
                
               
                var email = res.kakao_account.email;
                var name = res.properties.nickname;
                
                console.log(email);
                
              },
              fail: (res) => {
                console.log(res);
              },
            });
          },
        });
      }

      function kakaoLogout() {
        if (!Kakao.Auth.getAccessToken()) {
          alert("Not logged in.");
          return;
        }
        Kakao.Auth.logout(function () {
          alert("logout ok\naccess token -> " + Kakao.Auth.getAccessToken());
        });
      }
    </script>
    
	<button onclick="location.href='${contextPath}/Practice.do'">연습페이지이동</button>
</body>
</html>